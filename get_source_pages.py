import pywikibot

#הגדרת פונקציה
def get_page_text(page_title):
    """פונקציה שמקבלת שם של דף במכלול ומחזירה את קוד המקור שלו"""
    # הגדרת המכלול
    site = pywikibot.Site(url="https://www.hamichlol.org.il/")
    # קבלת הדף
    page = pywikibot.Page(site, title=page_title)
    #החזרת קוד המקור
    return page.text

print(get_page_text("החלף זאת בשם הערך"))
