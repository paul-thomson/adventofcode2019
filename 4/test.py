from main import check_if_valid_password, count_valid_passwords


def test_check_if_valid_password_1():
    expected_output = True

    actual_output = check_if_valid_password(111111)

    assert expected_output == actual_output


def test_check_if_valid_password_2():
    expected_output = False

    actual_output = check_if_valid_password(223450)

    assert expected_output == actual_output


def test_check_if_valid_password_3():
    expected_output = False

    actual_output = check_if_valid_password(123789)

    assert expected_output == actual_output


def test_count_valid_passwords_1():
    start = 100000
    end = 100001
    expected_output = 0

    actual_output = count_valid_passwords(start, end)

    assert actual_output == expected_output


def test_count_valid_passwords_2():
    start = 122456
    end = 122457
    expected_output = 2

    actual_output = count_valid_passwords(start, end)

    assert actual_output == expected_output


def test_count_valid_passwords_3():
    start = 123455
    end = 123460
    expected_output = 1

    actual_output = count_valid_passwords(start, end)

    assert actual_output == expected_output
