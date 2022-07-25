"""
. = any character except the new line

^ (The caret): Matches the char only at the beginning of the line

$: Matches at the end of the line

*: The preceding char should repeat 0 or more repetitions (greedy)

+: Matches 1 or more repetitions of the preceding expression
"""
import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \n" \
         "The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

result = re.search(r"(.+)", string)

print(result.groups(1))

# Search only 1 instance
result = re.search(r"^\w{3}", string)
print(result)

all_result = re.findall(r"^\w{3}", string, re.M)
print(all_result)

# Find the last word in the string
result = re.findall(r"\s(\w{2,})\W$", string, re.M)
print(result)

# search for 2 digits and possibly more than 2 digits
result = re.findall(r"\d\d\d*", string)
print(result)

# Find the words with E
# \w: Matches all alphanumeric characters

result = re.findall(r"E\w*", string)
print(result)

# Plus (+)

result = re.findall(r"\d\d\d+", string)
print(result)

result = re.findall(r"E\w+", string)
print(result)
