# importing regex module
import re

# Defining raw strings
# using 'r' before the string to classify it as a raw string
path = r"C:\Uses\tasks\new"

print(path)

# Compiling and finding
# Find the occurrence of 4-digit number
# Use compile method when you are searching for the target over and over again
# \d -  matches digits
string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

s = r"\d{4}"

t = re.compile(s)

result = re.findall(t, string)

print(result)

# Searching
# General Syntax
# re.search(pattern, string, flags)
# Scans through the entire target string and looks for the occurrences of the pattern that we specify as the first argument
# Finds the specified characters of the digits from the target string

search_result = re.search(r"\d{3}", string)
print(type(search_result))
print(search_result)

print(string[15:18])

# Matching
# Returns an object pattern if the pattern if located at the beginning of the string otherwise returns none
# \w  -any alphanumeric characters but not spaces

match_result = re.match(r"\w{3}", string)
print('Specifies if it is a match\n', type(match_result))
print(match_result)

# Full match
print(len(string))

# match the string of the specified length characters on the same line
print("Using fullmatch()")
full_match_result = re.fullmatch(r".{285}", string)
print(full_match_result)

# Find all
# Searches for and returns all the patterns found in the target string from left to right
print("Using findall()")
find_all_result = re.findall(r"\d{3}", string)
print(find_all_result)

# Split
# \s: matches any whitespace character

split_result = re.split(r"\s", string)

print(split_result)

# Substituting
# General syntax
# re.sub(pattern, replacement, string, count, flags)

# replace all the uppercase letters such as STOXX with "INDEX"
sub_result = re.sub(r"[A-Z]{2,}", "INDEX", string)
print(sub_result)

# Replace only 2 uppercase letters

sub_result_2 = re.sub(r"[A-Z]{2,}", "INDEX", string, 2)
print(sub_result_2)

# Variation of sub: subn
# Also specifies number of replacements made by the function

subn_result = re.subn(r"[A-Z]{2,}", "INDEX", string)
print(subn_result)

# group and groups
# .+ = anything and covers everything
# \d\d = 2 digits
# \s = whitespace
print("Using groups()")
group_result = re.search(r".+\s(.+ets).+(\d\d\s.+).", string)
# print(group_result)
print(group_result.groups())

# start end span
# start: specifies the start index of the word searched for
# end: specifies the end index of the word searched for
# span: returns both start and end index of the target string

start_index = group_result.start(1)
print(start_index)

end_index = group_result.end(1)
print(end_index)

# Sanity check
san = string[49:56]
print(san)

span = group_result.span(1)
print(span)

# Optional flags
# Top 3 flags: I, S, X
# I: Case insensitive matching
# S: DOT all (Covers up new line as well)
# X: Verbose (Better spaces and indentation)(Lets write comments within the pattern)

# Find "the" in the string

find_the = re.findall(r"the", string, re.I)

print(find_the)

# Detect new line

string2 = "Hello\nPython"

detect_1 = re.search(r".+", string2)
detect_2 = re.search(r".+", string2, re.S)
print(detect_1)
print(detect_2)

# Use verbose for better understanding of the code
# USing groups with better commenting
verbose_result = re.search(r""".+\s #String that starts with anything and covers everything until next part
                           (.+ex) # Searching for word ending with ex
                           .+ #Middle of the string
                           (\d\d\s.+). # Date at the end""", string, re.X)

print(verbose_result.groups())

