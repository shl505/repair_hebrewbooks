import re
#הגדרת מחלקה שמייצגת דף במכלול
class Page:

    def __init__(self, page_text):
        """פונקציה שמקבלת שם דף מחזירה קוד מקור של דף במכלול"""
        self.page_text = page_text

    #--------------------------------------------------------------------------------#

    def get_list_hybro_links(self):
        """פונקציה שמקבלת מחרוזת ומחזירה רשימה של כל הקישורים לאתר היברובוקס במחרוזת"""
        #הגדרת משתנה שמכיל מחרוזת רגולרית
        link_tamplate = r"\[http://(?:www\.)?hebrewbooks\.org/\d+\s\w+(?:\s\w+)*\]"
        #חיפוש המחרוזת הרגולרית והכנסת התוצאות לרשימה
        list_links = re.findall(link_tamplate, self.page_text)
        #החזרת הרשימה
        return list_links
    
    #--------------------------------------------------------------------------------#

page = Page(page_text="""
* '''פירוש רבנו חננאל''' על התלמוד, למסכתות: [http://hebrewbooks.org/34550 פסחים]

 [http://www.hebrewbooks.org/16207 בבא בתרא]

[http://www.hebrewbooks.org/16195 בבא מציעא], [http://www.hebrewbooks.org/16186 בבא קמא]

[http://www.hebrewbooks.org/16234 חולין],
""")

print(page.get_list_hybro_links())
