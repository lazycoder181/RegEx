"""
Extension Notations And Assertions
.+(\b.+ex\b).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.
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
