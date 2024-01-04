import re
import time
def is_valid_pass():
    with open ("password.txt", "a+") as passwords:
        lines = passwords.readlines()[1:]
        up = lambda x: 1 if re.search(r'[A-Z]',x) else 0
        low = lambda x: 1 if re.search(r'[a-z]',x) else 0
        nums = lambda x: 1 if re.search(r'[0-9]',x) else 0
        invalid_words = []
        for line in lines:
            pw = line.strip()
            match = up(pw)+low(pw)+nums(pw)

            if (match == 3 and (8 <= len(pw) <= 32)):
                for i in pw:
                    if i not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
                        invalid_words.append(pw)
                if pw in invalid_words:
                    continue
                else:
                    print("{0} YES".format(pw))
            if not(8 <= len(pw) <= 32) and pw not in invalid_words:
                invalid_words.append(pw)
                print("{0} NO".format(pw))
            if match != 3:
                if pw in invalid_words:
                    continue
                print('{0} NO'.format(pw))
                invalid_words.append(pw)
            if pw[0] in r'[0-9]' and pw in invalid_words:
                continue
            for i in pw:
                if pw not in invalid_words and not re.search(
                    r'[a-zA-Z0-9]', i
                ):
                    print("{0} NO".format(pw))
                    invalid_words.append(pw)
            if (
                not re.search(r'[a-zA-Z0-9]', i)
                and not 8 <= len(pw) <= 32
            ):
                print("{0} NO".format(pw))
is_valid_pass()

