import re
import sys


def isNone(regex, target):
    return re.search(regex, target) is None


def strengthCheck(password):

    requirements = {
        "capital_err": '[A-Z]',
        "lower_err": '[a-z]',
        "symbol_err": '\W',
        "numeric_err": '\d',
        "length_err": '[\d\w\W]{8,}',
    }
    error = {
        "capital_err": True,
        "lower_err": True,
        "symbol_err": True,
        "numeric_err": True,
        "length_err": True,
    }
    output = ''
 
    for key in requirements:
        error[key] = isNone(requirements[key], password)
        output += "{}: {}\n".format(key, error[key])
    return output


def main(argv):
    password = argv
    print(strengthCheck(password))

if __name__ == "__main__":
    main(sys.argv[1])
