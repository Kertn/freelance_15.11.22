import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook

fn = "data_4.xlsx"
wb = load_workbook(fn)
ws = wb["Sheet"]

urls = []


for i in range(4):
    url = "https://www.dpxpower.nl"

    req = requests.get(url=f"https://www.dpxpower.nl/dpxnew/new/bouw/diesel-generatoren,{i+1},generatoroutput_asc,search.html")

    soup = BeautifulSoup(req.content, "lxml")

    pred_url = soup.find_all("span", class_="field field_brandmodel")

    for i in pred_url:
        urls.append(url + i.find_next("a").get("href"))

for f in urls:

    gen = "-"
    brand = "-"
    motor = "-"
    freq = "-"
    emmis = "-"
    volt = "-"
    tank = "-"
    tottal = "-"
    afmet = "-"
    garan = "-"
    land = "-"
    extra = "-"
    over = "-"
    certif = "-"

    print(f)
    title = []
    value = []
    img = []
    img_str = ""

    r = requests.get(url=f)
    soup_page = BeautifulSoup(r.content, "lxml")

    data_title = soup_page.find_all("td", class_="header")
    data_value = soup_page.find_all("td", class_="cell1")
    img_page = soup_page.find_all("a", class_="thumb")


    for i in img_page:
        img.append(i.get("href"))

    for i in img:
        img_str += i
        img_str += ", "

    for i in data_value[:17]:
        value.append(i.find_next("span").text)

    # for i in data_title:
    #     if i.text == "Generator":
    #         gen()
    #     if i.text == "Motorfabrikant":
    #         motor()
    #     if i.text == "Frequentie":
    #         freq()
    #     if i.text == "Emissieklasse":
    #         emiss()
    #     if i.text == "Voltage":
    #         volt()
    #     if i.text == "Tank capaciteit":
    #         tank()
    #     if i.text == "Totaalgewicht GVW":
    #         totaal()
    #     if i.text == "Afmetingen (LxBxH)":
    #         Afrmet()
    #     if i.text == "Garantie":
    #         garant()
    #     if i.text == "Land van productie":
    #         land()
    #     if i.text == "Extra":
    #         extra()
    #     if i.text == "Certificaten":
    #         certif()
    count = 0

    for i in data_title:
        if i.text == "Generator":
            gen = data_value[count+3].text
        if i.text == "Brandstofverbruik":
            brand = data_value[count + 3].text
        if i.text == "Motorfabrikant":
            motor = data_value[count+3].text
        if i.text == "Frequentie":
            freq = data_value[count+3].text
        if i.text == "Emissieklasse":
            emmis = data_value[count+3].text
        if i.text == "Voltage":
            volt = data_value[count+3].text
        if i.text == "Tank capaciteit":
            tank = data_value[count+3].text
        if i.text == "Totaalgewicht GVW":
            tottal = data_value[count+3].text
        if i.text == "Afmetingen (LxBxH)":
            afmet = data_value[count+3].text
        if i.text == "Garantie":
            garan = data_value[count+3].text
        if i.text == "Land van productie":
            land = data_value[count+3].text
        if i.text == "Extra":
            extra = data_value[count+3].text
        if i.text == "Overige informatie":
            over = data_value[count + 3].text
        if i.text == "Certificaten":
            certif = data_value[count+3].text
        count += 1



    value = value[3:]

    value.append(gen)
    value.append(brand)
    value.append(motor)
    value.append(freq)
    value.append(emmis)
    value.append(volt)
    value.append(tank)
    value.append(tottal)
    value.append(afmet)
    value.append(garan)
    value.append(land)
    value.append(extra)
    value.append(over)
    value.append(certif)

    value.append(img_str)
    value.append(" ")

    ws.append(value)
    wb.save(fn)
wb.close()

