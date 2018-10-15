import re

#  Verify phone numbers 

# Phone numbers
# Formats:
# (xxx)-xxxx-xxxx 
# (xxxx)-xxx-xxxx 
# (xxxxx)-xxx-xxx 
# (xxxxx)-xxxxxx

# Mobile regex, in progress
# rm = '(0\d{10})|(\+?447\d{9})|(\+?44\(0\)\s?\d{10})'

# separator
sep = '(\s|-|\/|\\|\.)'
# 3 number area code
r0 = '\d{10}'
r3 = '((\d{3}|\(\d{3}\))%s(\d{4}%s\d{4}|\d{8}))' % (sep, sep)
# 4 number area code
r4 = '((\d{4}|\(\d{4}\))%s(\d{4}%s\d{3}|\d{3}%s\d{4}|\d{7}))' % (sep, sep, sep)
# 5 number area code
r5 = '((\d{5}|\(\d{5}\))%s(\d{3}%s\d{3}|\d{6}))' % (sep, sep)

# combine the possible arrangements of number input
rdt = '(%s|%s|%s|%s)' % (r0, r3, r4, r5)

searchstring = 'phone numbers: (01234) 567890sdfsd. 12345 555 555 or' \
    '(11111) 222333' \
    '12311114444 (124) 566633372343 ' \
    '1100 440 0000 asd(0000) 1234567asd' \
    'a10028 496986 (1100) 0120 030' \
    '01129-530-662'

# creating regex string when spaces are used
rt = '(\(?\d{3}\)?\s?\d{4}\s?\d{4}|\(?\d{4}\)?\s?(\d{3}\s?\d{4}|\d{4}\s?\d{3}|\d{7})|' \
      '\(?\d{5}\)?\s?(\d{3}\s?\d{3}|\d{6}))'

# Alternatively, use compile and verbose to create the regex
phoneRegex = re.compile(r'''(
    (\(?\d{3}\)?\s?\d{4}\s?\d{4}|
    \(?\d{4}\)?\s?(\d{3}\s?\d{4}|\d{7})|
    \(?\d{5}\)?\s?(\d{3}\s?\d{3}|\d{6})))''', re.VERBOSE)
result = phoneRegex.findall(searchstring)

# Create the search using combined regex
match = re.compile(rdt)
result = match.findall(searchstring)

for numbers in result:
    print(numbers[0])
