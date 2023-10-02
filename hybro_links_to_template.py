import re
#הגדרת מחלקה שמייצגת דף במכלול
class Page:

    def __init__(self, page_text):
        self.page_text = page_text #קבלת טקסט המקור של הדף


    def get_list_hybro_links(self):
        link_tamplate = r"\[http://(?:www\.)?hebrewbooks\.org/\d+\s\w+(?:\s\w+)*\]"
        list_links = re.findall(link_tamplate, self.page_text)
        return list_links

page = Page(page_text="""
* '''פירוש רבנו חננאל''' על התלמוד, למסכתות: [http://hebrewbooks.org/34550 פסחים]

 [http://www.hebrewbooks.org/16207 בבא בתרא]

[http://www.hebrewbooks.org/16195 בבא מציעא], [http://www.hebrewbooks.org/16186 בבא קמא]

[http://www.hebrewbooks.org/16234 חולין],
""")

print(page.get_list_hybro_links())