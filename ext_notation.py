"""
Extension Notations And Assertions

"""

import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."
# Non capturing groups: will not be retrieved
# Match the following groups:
# 1. words ending with 'ex'
# 2. Upper case letters with 4 chars
# 3. Chars starting with 2 digits and ending with anything

result = re.search(r".+(\b.+ex\b).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string)
print(result.groups(1))

# Blocking the first group by adding ?:

result = re.search(r".+(?:\b.+ex\b).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string)
print(result.groups())

# Named groups and groupdict()
# Syntax: ?P<name>
# Name the above groups


result = re.search(r".+(?P<wordex>\b.+ex\b).+(?P<uppercase>\b[A-Z]{4}\b).+(?P<date>\d\d\s.+)\.", string)
print(result.group("wordex"))

# groupdict() method
# Key value type

print(result.groupdict())

# Positive lookahead assertions
# 4 types: positive and negative for each lookahead and lookbehind assertions

# Positive lookahead assertions
# Syntax: (?=...)
# Match a 5 letter word if and only if it is followed by a 3 digit number

result = re.findall(r"[A-Z]{5}\s(?=[0-9]{3})", string)
print(result)

# Match Euro if and only if it is immediately followed by another letter

result = re.findall(r"Euro(?=[a-z]+)", string)
print(result)

# Negative lookahead assertions
# Returns a match if and only if the pattern inside the parenthesis does not follow the pattern before the parenthesis
# Syntax: ?!

# Match the a digit if it is not followed by a digit equal to and larger than 5 or a char which is not a digit

result = re.findall(r"\d(?![5-9]|\D)", string)
print(result)

# Match words that are not followed by a space

result = re.findall(r"\b\w+\b(?!\s)", string)
print(result)

# Positive lookbehind assertions
# Syntax:(?<=...)

result = re.findall(r"(?<=\s)\d{1,}", string)
print(result)

result = re.findall(r"(?<=,\s)\b\w+\b", string)
print(result)

#Negative lookbehind assertions
#Syntax: (?<!...)

result = re.findall(r"(?<!\s)\d{1,}", string)
print(result)

result = re.findall(r"(?<!x)x(?!x)", string, re.I)
print(result)

#Example
string_1 = "My favorite currency pairs are EURUSD, GBPUSD, USDCAD, AUDUSD, GBPEUR, NZDCHF and CHFJPY."
result = re.findall(r"(?<= )\w{3,}(?=\.)", string_1)
print(result)