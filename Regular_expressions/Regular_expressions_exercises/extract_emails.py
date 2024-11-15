# import re
#
# text = input()
# regex = r"^|\s(?P<email>[a-zA-Z\d]+[\.\-\_]*[a-zA-Z\d]*@[a-zA-Z]+[\-]*[a-zA-Z]*\.[\.a-zA-z]*[a-zA-Z])"
# matches = re.findall(regex, text)
#
#
# for match in matches:
#     print(match)


import re

text = input()
regex = r"\s[a-z0-9]+[a-z0-9\.\-\_]*@[a-z\-]+\.[a-z]+\.?[a-z]*\b"
matches = re.findall(regex, text)

for match in matches:
    print(match)
