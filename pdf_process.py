import pdfplumber
import re
# import fitz
def get_page_txt(page):
    str = ""
    page_left = page.crop((page.bbox[0],page.bbox[1], 0.5 * float(page.width), page.bbox[3]))
    page_right = page.crop((0.5 * float(page.width), page.bbox[1], page.width, page.bbox[3]))
    str += page_left.extract_text()
    str += page_right.extract_text()
    return str
def get_ref_pages(pdfname):
    with pdfplumber.open(pdfname) as pdf:
        page_num = len(pdf.pages)
        ref_num = page_num-1
        while ref_num > 0:
            ref_txt = get_page_txt(pdf.pages[ref_num])
            if "REFERENCE" in ref_txt or "References" in ref_txt:
                break
            else:
                ref_num -=1
        ref_info_txt = ""
        for num in range(ref_num,page_num):
            ref_info_txt += get_page_txt(pdf.pages[num])
    return ref_info_txt

        # with open("pdf_info.txt","w",encoding='utf_8') as fp:
        #     fp.write(page_left.extract_text())
        #     fp.write(page_right.extract_text())
        # print(first_page.extract_text())
    #     print(page.bbox)
    #     print(page.width)
    #     print(page.height)
    #     print(type(page_right.lines[0]))
    # print(page_right.lines[0])

def get_ref_list(references):
    references = references.replace("-\n","")
    references = references.replace("\n"," ")
    with open("pdf_info_afterprocess.txt","w",encoding='utf_8') as fp:
        fp.write(references)
    ref_pattern = re.compile(r'((\[[0-9]+\] )+.*?[0-9]+\.( \[Online\].*?\.pdf\.?)?( doi.*?\. )?)')
    ref_list = ref_pattern.findall(references)
    for num,element in enumerate(ref_list):
        ref_list[num] = element[0]
     
    with open("ref_info.txt","w",encoding='utf_8') as fp:
        fp.write(str(ref_list))
    return ref_list
# pdf_path = "pdf/Next-Generation_Healthcare_Enabling_Technologies_for_Emerging_Bioelectromagnetics_Applications.pdf"
# pdf_path = "pdf/Ten_Fundamental_Antenna-Theory_Puzzles_Solved_by_the_Antenna_Equation_A_remarkable_array_of_solutions.pdf"
pdf_path = "pdf/Tracking_Complete_Deformable_Objects_with_Finite_Elements.pdf"

# print(get_ref_pages(pdf_path))

ref_info = get_ref_pages(pdf_path)
get_ref_list(ref_info)
# with open("pdf_info.txt","w",encoding='utf_8') as fp:
#     fp.write(ref_info)
class pdfreference:
    def __init__(self, author, title, journal, pagenumber, date, doi, link):
        self.content = {}
        self.content["author"] = author
        self.content["title"] = title
        self.content["journal"] = journal
        self.content["pagenumber"] = pagenumber
        self.content["date"] = date
        self.content["doi"] = doi
        self.content["link"] = link
        return
    # def author
    # def show(self):
    #     print
    def downloadbib(self):

        return
    def __str__(self):
        return 'author: %s\ntitle: %s\njournal: %s\npagenumber: %s\ndate: %s\ndoi: %s\nlink: %s' \
        %(self.content["author"],self.content["title"],self.content["journal"],self.content["pagenumber"],self.content["date"],self.content["doi"],self.content["link"])
    
ref = pdfreference('zz', 'hello', 'ustc', '111', '2022.9','','')
ref.author = 'zzz'
print(ref)