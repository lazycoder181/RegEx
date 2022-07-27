import re

# Opening and reading the text file
f = open(r"bookshelf.txt")
string = f.read()
print(string)

# Match all the authors whose book titles are shorter than 25 chars
result = re.findall(r".+?;(.{1,25});.+?", string)
print(result)

# All the authors with the books published from the year 2000
result = re.findall(r"(.+?);.+?;20\d\d", string)
print(result)

