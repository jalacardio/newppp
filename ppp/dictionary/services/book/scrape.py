from bs4 import BeautifulSoup
import requests
import string
alphabet = string.ascii_uppercase

for alpha in alphabet:
    url = 'http://www.taiwantestcentral.com/WordList/WordListByName.aspx?MainCategoryID=4&Letter=' + alpha
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    easy = open("gept/easy.txt", "a")
    med = open("gept/medium.txt", "a")
    hard = open("gept/hard.txt", "a")

    content = soup.select('table.WordList.fg_highlight tr')
    skip = True
    for c in content:
        if skip:
            skip = False
            continue
        td = c.select('td')
        level = td[1].text
        word = td[3].text
        meaning = td[5].text

        if level == '初級':
            easy.write("{}, {}, {}\n".format(level, word, meaning))
        if level == '中級':
            med.write("{}, {}, {}\n".format(level, word, meaning))
        if level == '中高級':
            hard.write("{}, {}, {}\n".format(level, word, meaning))


    # for content in soup.select("td.nowrap.w1"):
    #     easy.write(content.text + "\n")
    # easy.close()
    #
    # for content in soup.select("td.nowrap.w2"):
    #     med.write(content.text + "\n")
    # med.close()
    #
    # for content in soup.select("td.nowrap.w3"):
    #     hard.write(content.text + "\n")
    # hard.close()
