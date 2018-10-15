import re

# USING SEARCH METHOD WITH REGEX

# Using phone number as an example, basic regex:
# r before string enters as raw string - doesn't escape characters
# checks for digits in the format 987-987-9876
phone = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Matches: 123-456-7890

# Using brackets creates groups that can be referenced
phone = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

# The brackets allow for grouping
# areaCode, mainNumber = mo.group(1), mo.group(2)
# print("Area Code: {}\nNumber: {}".format(areaCode, mainNumber))

# specify brackets in input with escape character
phone = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# Matches: (123)-456-7890

# specify alternative options, e.g . between numbers
phone = re.compile(r'(\d\d\d)(-|\.| )(\d\d\d(-|\.| )\d\d\d\d)')
# Matches: 123.123 1231

# specify optional search terms with (<search>)?
phone = re.compile(r'((\()?\d\d\d)(\))?(-|\.| )(\d\d\d(-|\.| )\d\d\d\d)')
# Matches (123)-456.7890 or 123 456-7890

# Match zero or more with *
phone = re.compile(r'((\()?\d\d\d)(\))?(-|\.| )*(\d\d\d(-|\.| )*\d\d\d\d)')
# Matches (123)456.7890 or 123 .456-7890 (no separator needed)

# Match one or more with +
phone = re.compile(r'((\()?\d\d\d)(\))?(-|\.| )+(\d\d\d(-|\.| )+\d\d\d\d)')
# Matches (123) 456.7890 or 123 .456-7890

# Match specific repititions with curly brackets
phone = re.compile(r'(((\()?(\d{3})(\))?(-|\.| )){2}\d{4})')
#                     |____||_____|     |_______||_||_____|
#       optional brackets      |        dividors  |   trailing digits
#                              |                  |
#                   set of 3 digits  repeat set of 3 followed by a dividor
# Matches (123).345-1231

# Use min max to specify a range of possible matches
# {, 3} = 0 to 3 matches, {3,} = 3 or more matches
phone = re.compile(r'(((\()?(\d{3,5})(\))?(-|\.| )){2}\d{4})')
# Matches 12345-345-3457

# By deafult, search is greedy. 
# Use ? to specify you want the min number of matches
# e.g:
phone = re.compile(r'(((\()?(\d{3,5})(\))?(-|\.| )){2}\d{4,}?)')
# passing  12380-345-12345678 Matches 12380-345-1234 with ? added
# This ? is unrelated to the optional operator.

# FINDALL 
phone = re.compile(r'((\d{3}(-|.| )){2}\d{4})')
searchstring = 'my number is 123-456-7890.' \
               'My other number is 486 234-1234'

print(phone.findall(searchstring))

# Common characters:
# \d Numeric from 0-9
# \D Not numeric 0-9
# \w Any letter, numeric digit or underscore (word)
# \W and character NOT \w
# \s any space, tab or newline
# \S any character NOT a space, tab or newline
# e.g. 
phone = re.compile(r'(\w+:\s(\d{3}(-|.| )){2}\d{4})')
# Matches: UK: 123-456-7890

# CHARACTER CLASSES
# [0-5] == (0|1|2|3|4|5)
# [a-zA-Z0-9] match all lower + upper letters, numbers
# inside [], regex symbols arent interpreted - no need to escape

