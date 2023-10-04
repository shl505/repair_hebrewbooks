import requests
from bs4 import BeautifulSoup
from repair_text import repair_text
import mwclient
from mwclient import Site
from mwclient import page

# המחרוזת שבה אתה מחפש
search_term = "hebrewbooks.org"


# ה-URL שבו מופיע המידע
url = f"https://www.hamichlol.org.il/w/index.php?title=%D7%9E%D7%99%D7%95%D7%97%D7%93:%D7%97%D7%99%D7%A4%D7%95%D7%A9_%D7%A7%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D_%D7%97%D7%99%D7%A6%D7%95%D7%A0%D7%99%D7%99%D7%9D&limit=2&offset=0&target={search_term}&namespace=0"
def bot(url:str):
    # שליחת בקשת HTTP GET ל-URL
    response = requests.get(url)
    # יצירת מבנה ה-BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # חיפוש על פי התגית "li" שמכילה את התוצאות
    results = soup.find_all('li')[1:]
    site = Site("www.hamichlol.org.il")
    site.login("שלוימי", "")
    for result in results:
        # בדיקה אם התוכן שבתוך ה-<li> מכיל את ה-search_term
        if search_term in result.text:  # חיפוש והשגת הלינק

            link = result.find('a', title=True)

            if link:
                # השגת הערך של ה-`title`
                title = link['title']
                title = "הגט מקליווא"
                # Connect to Wikipedia using pywikibot


                # Loop through each page title

                # Get the Wikipedia page object
                page = mwclient.page.Page(site, title)
                page_text = page.text()
                print(page_text)

                # Perform your edits, add new text, etc.
                # For example, adding a new line at the end of the page
                new_text = repair_text(page_text)

                # Save the updated page
                page.save(new_text, summary="תיקון בוט היברו בוקס") #הוספתי תקציר עריכה

                # Disconnect from Wikipedia

bot(url)