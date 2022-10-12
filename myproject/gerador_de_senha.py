import string
alphabet = string.ascii_letters + string.digits
password = ''.join(choice(alphabet) for i in range(8))