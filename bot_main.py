import requests
from bs4 import BeautifulSoup
import pywikibot
from repair_text2 import repair_text

# המחרוזת שבה אתה מחפש
search_term = "www.hebrewbooks.org"

# ה-URL שבו מופיע המידע
url = f"https://www.hamichlol.org.il/w/index.php?title=%D7%9E%D7%99%D7%95%D7%97%D7%93:%D7%97%D7%99%D7%A4%D7%95%D7%A9_%D7%A7%D7%99%D7%A9%D7%95%D7%A8%D7%99%D7%9D_%D7%97%D7%99%D7%A6%D7%95%D7%A0%D7%99%D7%99%D7%9D&limit=2&offset=0&target={search_term}&namespace=0"

# שליחת בקשת HTTP GET ל-URL
response = requests.get(url)

# יצירת מבנה ה-BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# חיפוש על פי התגית "li" שמכילה את התוצאות
results = soup.find_all('li')

for result in results:
    # בדיקה אם התוכן שבתוך ה-<li> מכיל את ה-search_term
    if search_term in result.text:  # חיפוש והשגת הלינק

        link = result.find('a', title=True)

        if link:
            # השגת הערך של ה-`title`
            title = link['title']

            # Connect to Wikipedia using pywikibot
            site = pywikibot.Site("www.hamichlol.org.il")
            site.login(username='שלוימי', password='AnotherPassword')
            strings = ["[http://www.hebrewbooks.org/", "[http://hebrewbooks.org/"]
            # Loop through each page title
            for i in title:
                # Get the Wikipedia page object
                page = pywikibot.Page(site, i)
                page_text = page.text

                # Perform your edits, add new text, etc.
                # For example, adding a new line at the end of the page
                new_text = page_text + repair_text(i ,strings)

                # Save the updated page
                page.text = new_text
                page.save("המרת קישורי היברובוקס לתבניות")

            # Disconnect from Wikipedia
            site.logout()
