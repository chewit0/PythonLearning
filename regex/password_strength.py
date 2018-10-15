import re
import sys
import getpass


def strengthCheck(password):
    '''
    Outputs the strength of provided password based on requiremnts
    e.g. Atleast one: Uppercase, lowercase, digit, symbol and length
    Provide the password when calling the script. e.g.
    python3 passwordStrength ' TestPassword123!'
    '''

    requirements = {
        "Uppercase Error": '[A-Z]',
        "Lowercase Error": '[a-z]',
        "Symbol Error": '\W',
        "Digit Error": '\d',
        "Length Error": '[\d\w\W]{8,}',
    }
    error = {
        "Uppercase Error": True,
        "Lowercase Error": True,
        "Symbol Error": True,
        "Digit Error": True,
        "Length Error": True,
    }
    output = '\n'

    for key in requirements:
        error[key] = re.search(requirements[key], password) is None
        output += "{}: {}\n".format(key, error[key])
    print(output)

strengthCheck(getpass.getpass("Enter Password: "))
