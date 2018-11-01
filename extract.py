from bs4 import BeautifulSoup
from bs4 import NavigableString
import requests
import re
import json
import os
import sys
import html
import logging


def surrounded_by_strings( tag ):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))


def excludeSpecial(string):
    pattern = "\t|\r|\n"
    string = re.sub(pattern, "", string)
    return html.unescape(string)


#Main
logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='main.log',
                    filemode='w')



urls = []
with open('F:\\Documents\\Project\\analysis_html\\package\\url.txt') as rfile:
    for f in rfile:
        # f = f.replace("\"", "")
        url = f.strip()
        urls.append(url)

# path = "F:\\Documents\\Project\\analysis_html\\package\\url.txt"
# for root, dirs, files in os.walk(path):
#     for file in files:
#         name = file.replace('.html', '')
#         filename = root + '\\' + file
for url in urls:
    page = requests.get(url)
    # page = "E:\\BaiduNetdiskDownload\\apps\\data\\air.com.arcadefest.jigsawpuzzles.html"
    # soup = BeautifulSoup(open(filename, encoding="ISO-8859-1"), "lxml")
    soup = BeautifulSoup(page.text, "lxml")
    for s in soup('script'):
        s.extract()
    html_nodes = soup.body.find_all()
    # a = soup.find_all_next(html_nodes[0])
    # html_nodes = soup.find_all(surrounded_by_strings)
    # print(html_nodes)
    result = list()
    temp_stack = list()



    #寻找标题
    title_set = set()
    #h标题
    h_nodes = soup.find_all(re.compile("^h[1-9]$"))



    for h_node in h_nodes:
        title_set.add(h_node)

    maybe_title_tag = ['strong', 'b', 'em']
    for tag in maybe_title_tag:
        tag_nodes = soup.find_all(tag)


        for i in tag_nodes:
            flag = True

            if flag:
                son_text = i.text

                try:
                    baba_p_text = i.find_parent("p").text.strip()
                except:
                    baba_p_text = ""

                try:
                    baba_div_text = i.find_parent("div").text.strip()
                except:
                    baba_div_text = ""

                # print(i.find_parent("div").string)

                if son_text == baba_p_text:
                    title_node = i.find_parent("p")
                    flag = True
                elif son_text == baba_div_text:
                    title_node = i.find_parent("div")
                    flag = True
                else:
                    title_node = ""
                    flag = False

                if '.' in son_text:
                    flag = False

                word_num = son_text.count(' ')

                if word_num > 10:
                    flag = False


            if flag > 0:
                # logging.
                title_set.add(title_node)



    for node in html_nodes:

        text = excludeSpecial(node.text).strip()
        if node in title_set:

            if len(temp_stack) > 0:
                result.append(temp_stack)
            temp_stack = [str(node)]


        else:

            if len(text) > 0 and len(temp_stack) > 0:
                temp_stack.append(str(node))
    result.append(temp_stack)

    paragraph_temp_stack = list()
    final_result = list()
    for paragraph in result:

        p = 0
        q = p + 1
        paragraph_len = len(paragraph)
        while q < paragraph_len:
            if paragraph[p].find(paragraph[q]) >= 0:
                # print(paragraph[p] + "\n &&& \n" + paragraph[q] + ";;;;;;\n\n\n\n")
                paragraph.remove(paragraph[q])
                paragraph_len = paragraph_len - 1

            else:
                p = q
                q = q + 1

            next_index = result.index(paragraph) + 1
            if next_index < len(result):
                if paragraph[p].find(result[next_index][0]) >= 0:
                    paragraph.remove(paragraph[p])
                    paragraph_len = paragraph_len - 1

        temp_paragraph = list()
        for word in paragraph:
            elem = dict()
            elem['value'] = word
            level = 0
            if paragraph.index(word) == 0:
                level = 1
                check_level = word[0:3]
                if re.match("^<h[1-9]$", check_level) is not None:
                    level = 10 - int(word[2])

            elem['level'] = level
            temp_paragraph.append(elem)

        final_result.append(temp_paragraph)

    name = url.replace('.', '_').replace('/', '_')
    fo = open("./set2/" + name + ".json", "w")
    fo.write(json.dumps(final_result))
    fo.close()
