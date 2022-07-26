"""
. = any character except the new line

^ (The caret): Matches the char only at the beginning of the line

$: Matches at the end of the line

*: The preceding char should repeat 0 or more repetitions (greedy)

+: Matches 1 or more repetitions of the preceding expression

?: Matches 0 or 1 repetitions of the preceding expression
    The question mark after the asterisk, plus sign or question mark turns off the greedy behaviour completely
    *? or +? or ??

\: Signals a special sequence (\d, \w, etc)
   Escaping and matching a symbol with special meaning in regex syntax (\. or \?)

[]: represent sets of chars and char classes
"""
import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

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

# search for 0 or 1 digits
result = re.findall(r"\d\d\d?", string)
print(result)

# Cancels the greedy behaviour
result = re.findall(r"E.? ", string)
print(result)

result = re.findall(r"E\w?", string)
print(result)

# Cancelling greedy behaviour
# Matching first two chars
result = re.findall(r"\d\d\d*?", string)
print(result)

# Matching first three chars
result = re.findall(r"\d\d\d+?", string)
print(result)

# 0 repetitions only

result = re.findall(r"\d\d\d??", string)
print(result)

# Finding . chars in the string
result = re.findall(r"\.", string)
print(result)

# Finding chars in the target string

result = re.findall(r"[wxkq]", string)
print(result)

# Specifying range of chars (occurences of a,b,c,d)

result = re.findall(r"[a-d]", string)
print(result)

result = re.findall(r"[0-4]", string)
print(result)

# Two ranges

result = re.findall(r"[a-f][c-w]", string)
print(result)

result = re.findall(r"[0-5][7-9]", string)
print(result)

# Combining digits with letters

result = re.findall(r"[0-9][a-z]", string)
print(result)

# Negation(every char except...)

result = re.findall(r"[^X]", string)
print(result)
print("X" in result)

# Character classes

# All nums in the target string

result = re.findall(r"[0-9]", string)
print(result)

# All alphabets in the target string
result = re.findall(r"[a-zA-Z]", string)
print(result)

# All chars except nums

result = re.findall(r"[^0-9]", string)
print(result)

# All whitespaces

result = re.findall(r"[ \n\t\r\f\v]", string)
print(result)

# Verfying the number of whiote spaces
print(len(result))
print(string.count(" "))

# Everything except whitespace
result = re.findall(r"[^ \n\t\r\f\v]", string)
print(result)

# All the occurrences of digit and letters in the target string except for whitespaces
result = re.findall(r"[a-zA-Z0-9_]", string)
print(result)

# Negation of the above to get whitespaces and symbols used in the target string

result = re.findall(r"[^a-zA-Z0-9_]", string)
print(result)

