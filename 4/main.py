def check_if_valid_password(password: int, additional=False) -> bool:
    if len(str(password)) != 6:
        return False

    any_digit_adjacency = False
    str_password = str(password)
    for i, letter in enumerate(str_password):
        # is letter the same as previous letter
        if i > 0:
            previous_letter = str_password[i - 1]
            if letter == previous_letter:
                if additional:
                    if i > 1:
                        if letter == str_password[i - 2]:
                            continue
                    if i < len(str_password) - 1:
                        if letter == str_password[i + 1]:
                            continue
                any_digit_adjacency = True
    if not any_digit_adjacency:
        return False

    for i, letter in enumerate(str_password):
        # are digits non-decreasing
        if i > 0:
            previous_letter = str_password[i - 1]
            if int(letter) < int(previous_letter):
                return False

    return True


def count_valid_passwords(start: int, end: int, additional=False) -> int:
    counter = 0
    for i in range(start, end + 1):
        if check_if_valid_password(i, additional=additional):
            counter += 1

    return counter


if __name__ == "__main__":
    print(count_valid_passwords(171309, 643603))
    print(count_valid_passwords(171309, 643603, additional=True))
