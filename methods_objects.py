# importing regex module
import re

# Defining raw strings
# using 'r' before the string to classify it as a raw string
path = r"C:\Uses\tasks\new"

print(path)

# Compiling and finding
# Find the occurence of 4 digit number
# Use compile method when you are searching for the target over and over again

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

s = r"\d{4}"

t = re.compile(s)

result = re.findall(t, string)

print(result)


