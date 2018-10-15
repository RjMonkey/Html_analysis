from bs4 import BeautifulSoup
import requests
import re
import json
import os
import sys
import html
import pprint


def excludeSpecial(string):
    pattern = "\t|\r|\n"
    string = re.sub(pattern, "", string)
    return html.unescape(string)


def isTitle(temp_node, title_set):


    tag = temp_node.name
    if re.match(r"^h[1-9]$", tag):
        # print(tag)
        return True

    elif temp_node.string in title_set:
        return True

    else:
        return False


page = requests.get("http://www.wechat.com/mobile/htdocs/en/privacy_policy.html#pp_how")
# page = "E:\\BaiduNetdiskDownload\\apps\\data\\air.com.arcadefest.jigsawpuzzles.html"
bsObj = BeautifulSoup(page.text, "lxml")
bsObj = html.unescape(bsObj)

for s in bsObj('script'):
    s.extract()

# 识别标题标签集合，用来判断标签是否为标题
try:
    bsObj.footer.decompose()

except:
    pass

html_nodes = bsObj.find_all()

# attribute_list = ['class', 'id', 'value', 'href', 'disabled', 'hidden', 'selected', 'for', 'src', 'name', 'style', 'title', 'target']
result = list()

temp_stack = list()

# 找标题
strong_nodes = bsObj.find_all("strong")
title_set = set()

for i in strong_nodes:
    son_text = i.string
    baba_text = i.parent.string
    if son_text == baba_text:
        title_set.add(son_text)

# temp_title_set = set()

for node in html_nodes:

    node.string = excludeSpecial(node.text)

    text = str(node.text).strip()
    elem = {"value": text, "tag": node.name}

    if isTitle(node, title_set):

        if len(temp_stack) > 0:
            result.append(temp_stack)
        temp_stack = [elem]
        # temp_title_set.add(text)

    else:
        if len(text) > 0 and len(temp_stack) > 0:
            temp_stack.append(elem)

result.append(temp_stack)
pass
