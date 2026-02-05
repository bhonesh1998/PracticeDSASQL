
import re

text = "  man can not die until and unless he is worried "
pattern = r"[a-z]+an"

# pattern1 = "mann"
#
# print(re.search(pattern1,text))

ma = (re.finditer(pattern,text))


for i in ma:
    print(i.span())
    print(text[i.span()[0]:i.span()[1]])

