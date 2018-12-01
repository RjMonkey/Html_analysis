#
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re


def remove_punctuation(line):
    rule = re.compile(r"[^a-zA-Z0-9\u4e00-\u9fa5]")
    line = rule.sub('', line)
    return line


example_sent = "- Find Accounts on the Device"

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)

title_str = (' '.join(filtered_sentence)).strip()
print(title_str)
# import re
#
#
# def remove_punctuation(line):
#     rule = re.compile(r"[^a-zA-Z\u4e00-\u9fa5]")
#     line = rule.sub('', line)
#     return line
#
#
# ele = "6.CHILDREN'S PRIVACY"
# print(remove_punctuation(ele))


