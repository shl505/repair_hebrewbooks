import requests
from bs4 import BeautifulSoup
from repair_text import repair_text
import mwclient
from mwclient import Site
from mwclient import page

def bot():
    # ה-URL שבו מופיעה רשימת הקישורים
    url = [
        "https://www.hamichlol.org.il/w/index.php?title=%D7%9E%D7%99%D7%95%D7%97%D7%93:%D7%97%D7%99%D7%A4%D7%95%D7%A9_%D7%A7%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D_%D7%97%D7%99%D7%A6%D7%95%D7%A0%D7%99%D7%99%D7%9D&limit=2&offset=0&target=hebrewbooks.org&namespace=0"#,
        #"https://www.hamichlol.org.il/w/index.php?title=%D7%9E%D7%99%D7%95%D7%97%D7%93:%D7%97%D7%99%D7%A4%D7%95%D7%A9_%D7%A7%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D_%D7%97%D7%99%D7%A6%D7%95%D7%A0%D7%99%D7%99%D7%9D&limit=2&offset=0&target=www.hebrewbooks.org&namespace=0"
    ]
    for i in url:
        # המחרוזת לחיפוש
        search_term = "hebrewbooks.org"
        # שליחת בקשת HTTP GET ל-URL
        response = requests.get(i)
        # יצירת מבנה ה-BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # חיפוש על פי התגית "li" שמכילה את התוצאות
        results = soup.find_all('li')[1:]
        # הURL של המכלול
        site = Site("www.hamichlol.org.il")
        # שם משתמש וסיסמה של הבוט
        site.login("שלוימי", "")
        # לולאה על רסימת הדפים
        for result in results:
            # בדיקה אם התוכן שבתוך ה-<li> מכיל קישור ליברובוקס
            if search_term in result.text:
                # חיפוש והשגת הלינק
                link = result.find('a', title=True)

                if link:
                    # השגת הערך של ה-`title`
                    title = link['title']
                    title = "משתמש:שלוימי/טיוטה"
                    #
                    page = mwclient.page.Page(site, title)
                    # השגת קוד המקור של הערך
                    page_text = page.text()
                    # השגת הטקסט המתוקן באמצעות הפונקציה repair_text
                    new_text = repair_text(page_text)
                    # שמירת הערך עם הקוד המעודכן
                    page.save(new_text, summary="המרת קישורי היברובוקס לתבנית")  # הוספת תקציר עריכה
bot()