from bs4 import BeautifulSoup
from bs4 import NavigableString
import requests
import re
import json
import os
import sys
import html
import logging


def surrounded_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))


def updateTitle(tag_name, soup, title_set):

    strong_nodes = soup.find_all(tag_name)

    # soup.table.decompose()

    for i in strong_nodes:
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


            if son_text == baba_p_text or son_text == baba_div_text:

                flag = True
            else:
                flag = False

            if '.' in son_text:
                flag = False

            word_num = son_text.count(' ')

            if word_num > 10:
                flag = False



        # if flag:
        #     try:
        #         a = i
        #         for j in range(0, 20):
        #
        #             a = a.find_previous(recursive=False)
        #             if len(excludeSpecial(a.text)) > 0:
        #                 # lalaname = a.name
        #                 if a.name == tag_name:
        #                     flag = False
        #                 break
        #     except:
        #         print("No Such previous node")
        #
        # if flag:
        #     try:
        #         a = i
        #         for j in range(0, 20):
        #
        #             a = a.find_next(recursive=False)
        #             if len(excludeSpecial(a.text)) > 0:
        #                 if a.name == tag_name:
        #                     flag = False
        #                 break
        #     except:
        #         print("No Such next node")

        if flag:
            # logging.info("i :" + str(i))
            title_set.append(i.text.strip())



def excludeSpecial(string):
    pattern = "\t|\r|\n"
    string = re.sub(pattern, "", string)
    return html.unescape(string)


def isTitle(temp_node, title_set):
    tag = temp_node.name
    if re.match(r"^h[1-9]$", str(tag)):
        # print(tag)
        return True

    elif temp_node.string in title_set:
        return True

    else:
        return False


#Main
logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='main.log',
                    filemode='w')

page = requests.get("http://www.wechat.com/mobile/htdocs/en/privacy_policy.html#pp_how")
# page = "E:\\BaiduNetdiskDownload\\apps\\data\\air.com.arcadefest.jigsawpuzzles.html"
bsObj = BeautifulSoup(page.text, "lxml")
bsObj = html.unescape(bsObj)


for s in bsObj('script'):
    s.extract()



result = list()
temp_stack = list()
# 找标题
# 识别标题标签集合，用来判断标签是否为标题
tag_set = set()
temp_set = bsObj.find_all(re.compile("^h[1-9]$"))
for tag in temp_set:
    tag_set.add(tag.name)
tag_set.add("strong")
tag_set.add("em")
tag_set.add("b")

title_set = list()
updateTitle("strong", bsObj, title_set)

# print(json.dumps(list(title_set)))

# 遍历
html_nodes = bsObj.body.find_all(surrounded_by_strings)

for node in html_nodes:
    text = excludeSpecial(node.text).strip()
    elem = {"value": text, "tag": node.name}

    if isTitle(node, title_set):

        if len(temp_stack) > 0:
            result.append(temp_stack)
        temp_stack = [elem]

    else:
        if len(text) > 0 and len(temp_stack) > 0:
            temp_stack.append(elem)
    # next_node = node.next_element
    # if str(node).find(str(next_node)) >= 0:
    #
    #     # 格式化字符串
    #     # node.string = excludeSpecial(node.text).strip()
    #     logging.info("node : " + str(node) + "next : " + str(next_node))

    result.append(node)

    


# result.append(temp_stack)
pass
