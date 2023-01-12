from cnpgen import Cnp
import re


def check_phone_number(string):
    if len(string)!=10:
        return False



    if any(c not in '0 1 2 3 4 5 6 7 8 9' for c in string):
        return False

    if string[0]!='0' or string[1]!='7':
        return False
    return True


def check_CNP_lib(string):

    return Cnp.is_valid(string)

def check_CNP(string):
    if re.match(r"^[1-9]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d$",string):
        return True
    return False