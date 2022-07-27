import re
f = open("phone.txt")
string = f.read()

print(string)

#Match the last name and ph no whose area code end with 0

result = re.findall(r".+ (.+?)\t\(\d\d0\)\s(.+)", string)
print(result)

#Match Area code of each ph number that ends with 7

result = re.findall(r".+ .+\t\((.+)\)\s.{7}7", string)
print(result)

# Match all the first and last names whose phn nos start with odd nos (1,3,5,7,9)

result = re.findall(r"(.+)\t\(\d{3}\)\s[13579].{7}", string)
print(result)

# Match all first names whose area code number < 300

result = re.findall(r"(.+) .+\t\([0-2]\d\d\)\s.{8}", string)
print(result)

# Match all first names whose last name ends in a vowel and ph no ends in either 0 or 7 or 9

result = re.findall(r"(.+) .+[aeiou]\t\(\d{3}\) .{7}[079]", string)
print(result)