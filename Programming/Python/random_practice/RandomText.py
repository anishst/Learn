import string
import random
def random_generator(size=6, chars=string.ascii_uppercase + string.digits + "!@#$%^&*()_+-=\n\t"):
	return ''.join(random.choice(chars) for x in range(size))

print("default value")
print(random_generator())
print('custome')
print(random_generator(10, "1234"))


def getAlphaNumeric(length, type='letters'):
    """
    Get random string of characters

    :param length: length of string
    :param type: type of characters
    :return:
    """

    alpha_num = ''
    if type == 'lower':
        case = string.ascii_lowercase
    elif type == 'upper':
        case = string.ascii_uppercase
    elif type == 'digits':
        case = string.digits
    elif type == 'mix':
        case = string.ascii_letters + string.digits
    else:
        case = string.ascii_letters

    return alpha_num.join(random.choice(case) for i in range(length))


print(getAlphaNumeric(3, "mix"))