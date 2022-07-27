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

# Problem 1:
# Match all the book titles that end with letter p

result = re.findall(r".+?;(.+p);.+?", string)
print(result)

# Problem 2:
# Match the Authors whose last name starts with  the letter B

result = re.findall(r".+?(B.+);.+?;.+?", string)
print(result)

#Problem 3:
# match all the books published between 1980 and 1999

result = re.findall(r".+?;(.+?);19[8-9][0-9]", string)
print(result)