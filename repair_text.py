import pywikibot

def repair_text(repaired_text: str):
    """פונקציה שמקבלת קוד מקור של דף באתר המכלול וחזירה אותו לאחר שהמירה קישורים לאתר היברובוקס לתבניות קישורים"""
    #הגדרת משתנה שמכיל את הטקסט המקורי
    parts = repaired_text
    #הגדרת משתנה מטיפוס רשימה שמכיל את ראשי הקישורים
    strings = ["[http://www.hebrewbooks.org/", "[http://hebrewbooks.org/"]
    #הגדרת משתנה שמכיל את ראש התבנית
    string_repair = "{{היברובוקס||"
    #הגדרת לולאה שרצה פעם אחת על כל ראש קישור
    for string in strings:
        #בדיקה אם יש קישור בערך
        if string and repaired_text.find(string) >= 0:
            #הגדרת משתנה שסופר כמה קישורים יש בערך
            number = repaired_text.count(string)
            #הגדרת לולאה שרצה כמספר הקישורים שיש בערך
            for i in range(number):
                #עדכון המשתנה עם הקוד מקור של הערך לקוד מקור המתוקן
                parts = repaired_text
                #הגדרת משתנה עם טיפוס הקישור של pagefeed
                pagefeed = "pagefeed/hebrewbooks"
                #בדיקה אם יש בערך קישור מטיפוס pagefeed
                if string + pagefeed in parts:
                    list1 = parts.split(string + pagefeed, 1)
                    repair_pagefeed = list1[1].split("_", 3)
                    page_number = repair_pagefeed[3].split(".pdf", 1)
                    name = page_number[1].split("]", 1)
                    if name[0].count("[") == 0:
                        repaired_text = list1[0] + string_repair + name[0][1:] + "|" + repair_pagefeed[2] + "||ללא|עמוד=" + page_number[0] + "}}" + name[1]
                #בדיקה אם יש קישור מטיפוס pdfpager בטקסט
                elif "pdfpager.aspx" in parts:
                    #הגדרת משתנים שמכילים את טיפוסי הקישורים האפשריים בpdfpager
                    pdfpager_req = "pdfpager.aspx?req="
                    pdfpager_sits = "pdfpager.aspx?sits"
                    if string + pdfpager_req in parts:
                        repair_pdfpager = parts.split(string + pdfpager_req, 1)
                        if "&pgnum=" in repair_pdfpager[1]:
                            repair_page = repair_pdfpager[1].split("&pgnum=", 1)  # חיתוך לפני מיקום מספר העמוד
                            name = repair_page[1].split(" ", 1)
                            caption = name[1].split("]", 1)
                            if "&st=" in repair_page[0]:
                                repair_st = repair_page[0].split("&st=", 1)
                                if "&hilite=" in repair_st[0]:
                                    repair_hilite = repair_st[0].split("&hilite=", 1)
                                    repair_page[0] = repair_hilite[0]
                                else:
                                    repair_page[0] = repair_st[0]
                            if "&hilite=" in name[0]:
                                repair_hilite = name[0].split("&hilite=", 1)
                                name[0] = repair_hilite[0]
                            if caption[0].count("[") == 0:
                                repaired_text = repair_pdfpager[0] + string_repair + caption[0] + "|" + repair_page[0] + "||ללא|עמוד=" + name[0] + "}}" + caption[1]
                        else:
                            name = repair_pdfpager[1].split(" ", 1)
                            caption = name[1].split("]", 1)
                            if "&st=" in name[0]:
                                repair_st = name[0].split("&st=", 1)
                                if "&hilite=" in repair_st[0]:
                                    repair_hilite = repair_st[0].split("&hilite=", 1)
                                    name[0] = repair_hilite[0]
                                else:
                                    name[0] = repair_st[0]
                            if "&hilite=" in name[0]:
                                repair_hilite = name[0].split("&hilite=", 1)
                                name[0] = repair_hilite[0]
                            if caption[0].count("[") == 0:
                                repaired_text = repair_pdfpager[0] + string_repair + caption[0] + "|" + name[0] + "||ללא}}" + caption[1]

                    elif string + pdfpager_sits in parts:
                        repair_sits = parts.split(string + pdfpager_sits, 1)
                        repair_pdfpager = repair_sits[1].split("&req=", 1)
                        if "&pgnum=" in repair_pdfpager[1]:
                            repair_page = repair_pdfpager[1].split("&pgnum=", 1)  # חיתוך לפני מיקום מספר העמוד
                            name = repair_page[1].split(" ", 1)
                            caption = name[1].split("]", 1)
                            if "&st=" in repair_page[0]:
                                repair_st = repair_page[0].split("&st=", 1)
                                if "&hilite=" in repair_st[0]:
                                    repair_hilite = repair_st[0].split("&hilite=", 1)
                                    repair_page[0] = repair_hilite[0]
                                else:
                                    repair_page[0] = repair_st[0]
                            if "&hilite=" in name[0]:
                                repair_hilite = name[0].split("&hilite=", 1)
                                name[0] = repair_hilite[0]
                            if caption[0].count("[") == 0:
                                repaired_text = repair_sits[0] + string_repair + caption[0] + "|" + repair_page[0] + "||ללא|עמוד=" + name[0] + "}}" + caption[1]
                        else:
                            name = repair_pdfpager[1].split(" ", 1)
                            caption = name[1].split("]", 1)
                            if "&st=" in name[0]:
                                repair_st = name[0].split("&st=", 1)
                                if "&hilite=" in repair_st[0]:
                                    repair_hilite = repair_st[0].split("&hilite=", 1)
                                    name[0] = repair_hilite[0]
                                else:
                                    name[0] = repair_st[0]
                            if "&hilite=" in name[0]:
                                repair_hilite = name[0].split("&hilite=", 1)
                                name[0] = repair_hilite[0]
                            if caption[0].count("[") == 0:
                                repaired_text = repair_sits[0] + string_repair + caption[0] + "|" + name[0] + "||ללא}}" + caption[1]

                elif string in parts:
                    if string + "rambam" and string + "root" and string + "shas" and string + "journals" and string + "media/terms.html" and string + "hagada" and string + "dtrambam" and string + "home.aspx" and string + "j" and string + "download" and string + "about" and string + "english" and string + "about" and string + "media" not in parts:
                        list1 = parts.split(string, 1)
                        parts2 = list1[1].split(" ", 1)
                        list_descript_book = parts2[1].split("]", 1)
                        if list_descript_book[0].count("[") == 0:
                            repaired_text = list1[0] + string_repair + list_descript_book[0] + "|" + parts2[0] + "||ללא}}" + list_descript_book[1]

    if "{{ללא בוט}}" in parts:
        return parts

    else:
        return repaired_text

def get_page_text(page_title):
    """פונקציה שמקבלת שם של דף במכלול ומחזירה את קוד המקור שלו"""
    # הגדרת המכלול
    site = pywikibot.Site(url="https://www.hamichlol.org.il/")
    # קבלת הדף
    page = pywikibot.Page(site, title=page_title)
    #החזרת קוד המקור
    return page.text

#page_title = input("הכנס את שם הערך כאן: ")

#string = get_page_text(page_title)

#string = """[http://www.hebrewbooks.org/pdfpager.aspx?sits=1&req=20409&st=%u05e7%u05de%u05d9%u05e0%u05e6%u05e7%u05d9 יונמחמךל]"""

#print()
#print("------")
#print()
#print(repair_text(string))
#print()
#print("------")
