from get_source_pages import get_page_text
strings = ["[http://www.hebrewbooks.org/", "[http://hebrewbooks.org/" ]
string_repair = "{{היברובוקס||"


def repair_text(repaired_text: str, strings: list):
    for string in strings:
        if string and repaired_text.find(string) >= 0:
            number = repaired_text.count(string)

            for i in range(number):
                parts = repaired_text

                if "pagefeed/hebrewbooks_org" in parts:
                    if "[http://www.hebrewbooks.org/pagefeed/hebrewbooks" in parts:
                        list1 = parts.split("[http://www.hebrewbooks.org/pagefeed/hebrewbooks", 1)
                        repair_pagefeed = list1[1].split("_", 3)
                        page_number = repair_pagefeed[3].split(".pdf", 1)
                        name = page_number[1].split("]", 1)
                        repaired_text = list1[0] + string_repair + name[0][1:] + "|" + repair_pagefeed[2] + "||ללא|עמוד=" + page_number[0] + "}}" + name[1]
                    elif "[http://hebrewbooks.org/pagefeed/hebrewbooks" in parts:
                        list1 = parts.split("[http://hebrewbooks.org/pagefeed/hebrewbooks", 1)
                        repair_pagefeed = list1[1].split("_", 3)
                        page_number = repair_pagefeed[3].split(".pdf", 1)
                        name = page_number[1].split("]", 1)
                        repaired_text = list1[0] + string_repair + name[0][1:] + "|" + repair_pagefeed[2] + "||ללא|עמוד=" + page_number[0] + "}}" + name[1]
                elif "pdfpager.aspx" in parts:
                    if "[http://www.hebrewbooks.org/pdfpager.aspx" in parts:
                        repair_pdfpager = parts.split("[http://www.hebrewbooks.org/pdfpager.aspx?req=", 1)
                        repair_page = repair_pdfpager[1].split("&pgnum=", 1)  # חיתוך לפני מיקום מספר העמוד
                        name = repair_page[1].split(" ", 1)
                        caption = name[1].split("]", 1)
                        if "&st=" in repair_page[0]:
                            repair_st = repair_page[0].split("&st=", 1)
                            if "&hilite=" in repair_st [0]:
                                repair_hilite = repair_st [0].split("&hilite=", 1)
                                repair_page[0] = repair_hilite[0]
                            else:
                                repair_page[0] = repair_st[0]
                        if "&hilite=" in name[0]:
                            repair_hilite = name[0].split("&hilite=", 1)
                            name[0] = repair_hilite[0]
                        repaired_text = repair_pdfpager[0] + string_repair + caption[0] + "|" + repair_page[0] + "||ללא|עמוד=" + name[0] + "}}" + caption[1]
                    elif "[http://hebrewbooks.org/pdfpager.aspx" in parts:
                        repair_pdfpager = parts.split("[http://hebrewbooks.org/pdfpager.aspx?req=", 1)
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
                        repaired_text = repair_pdfpager[0] + string_repair + caption[0] + "|" + repair_page[0] + "||ללא|עמוד=" + name[0] + "}}" + caption[1]

                elif "[http://www.hebrewbooks.org/" in parts:
                    list1 = parts.split("[http://www.hebrewbooks.org/", 1)
                    parts2 = list1[1].split(" ", 1)
                    list_descript_book = parts2[1].split("]", 1)
                    if list_descript_book[0].count("[") == 0:
                        repaired_text = list1[0] + string_repair + list_descript_book[0] + "|" + parts2[0] + "||ללא}}" + list_descript_book[1]
                elif "[http://hebrewbooks.org/" in parts:
                    list1 = parts.split("[http://hebrewbooks.org/", 1)
                    parts2 = list1[1].split(" ", 1)
                    list_descript_book = parts2[1].split("]", 1)
                    if list_descript_book[0].count("[") == 0:
                        repaired_text = list1[0] + string_repair + list_descript_book[0] + "|" + parts2[0] + "||ללא}}" + list_descript_book[1]


    return repaired_text




page_title = input("הכנס את שם הערך כאן: ")

string = get_page_text(page_title)

print()
print("------")
print()
print(repair_text(string, strings))
print()
print("------")