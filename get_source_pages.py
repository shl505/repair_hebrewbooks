import pywikibot

#הגדרת פונקציה
def get_page_text(page_title):
    site = pywikibot.Site(url="hamichlol.org.il") # הגדרת המכלול
    page = pywikibot.Page(site, title=page_title) #קבלת הדף
    return page.text

print(get_page_text("תחיל את זה בשם הערך"))