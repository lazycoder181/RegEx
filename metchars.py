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

{}: Repeating the preceding char in a regex pattern along with * and + sign. More granular. Enables inserting 1 or 2 nos in the string

\b: Defines the borders of the words

| (The pipe): A|B|C (either a or b or c is matched, not all of the them)

\A: Matches only at the beginning of the string in the multiline string (re.M)

\Z: Matches only at the end of the string in (re.M)

\B: find subset of a word

\d: matches any digits from 0-9 char class

\D: matches any non-digit chars ( equivalent to [^0-9] )

\s: matches any whitespace chars

\S: matches any non-whitespace chars

\w: matches all word chars

\W: matches all non-word chars

"""
import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998.\nThe panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

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

# Verfying the number of white spaces
# Keep a count
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

# All the 4 letter words
result = re.findall(r"\b\w{4}\b", string)
print(result)

# Words with either 3, 4 or 5 chars

result = re.findall(r"\b\w{3,5}\b", string)
print(result)

# Words from atleast 3 chars
result = re.findall(r"\b\w{3,}\b", string)
print(result)

# The pipe
# Find any word with 3 chars or any word with 4 chars or any upper case 4 letter words
result = re.findall(r"\d{3}|\d{4}|\b[A-Z]{4}\b", string)
print(result)

# Words with atleast 10 characters

result = re.findall(r"\b\w{10,}\b", string)
print(result)

# Find Euro

result = re.findall(r"\bEuro\b", string)
print(result)

# Detect a subset of a word at the end of that word
result = re.findall(r"\Bcross", string)
print(result)

# Detect a subset of a word at the start of that word
result = re.findall(r"cross\B", string)
print(result)

# Detect a subset of a word somewhere in the middle of that word
result = re.findall(r"\Bcross\B", string)
print(result)

# detect only the digit followed by any lower case letters
# Output should only be the digit and not the letter following it. Use '()' for that

result = re.findall(r"(\d)[a-z]", string)
print(result)

# Match non-numeric digits between 2 non-alphanumeric chars

result = re.findall(r"\W\D\W", string)
print(result)

# MAtch all whitespace chars

result = re.findall(r"\s", string)
print(result)

# 8 or more non white space chars
result = re.findall(r"\S{8,}", string)
print(result)

# Match any set of 3-5 alphanumeric chars positioned in between white spaces

result = re.findall(r"\s(\w{3,5})\s", string)
print(result)
