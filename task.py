# flake8: noqa: C901

# Group Members : Clinton Lohr, Brian Haug, Gregory Monteleone
# Date          : 03/01/2023
# Course        : CS 362 - Software Engineering II
# Assignment    : Group Project

def conv_num(num_str):
    """
    This function takes in a string as the parameter and converts it into a base 10 number.
    Returns the base 10 number if input string was valid, otherwise 'None' is returned.
    """

    # Initial check to verify that num_str parameter is a string type
    if not num_str or not isinstance(num_str, str):
        return None

    is_neg_num = False
    is_float_num = False
    is_hex_num = False
    return_num = 0
    num_str_upper = num_str.upper()

    # Immediately converts integer if input string length is 1
    if len(num_str_upper) < 2:
        return conv_int(num_str, 1, return_num, is_neg_num)

    # Checks for negative number character '-'
    if num_str_upper[0] == '-':
        num_str_upper = num_str_upper[1:]
        is_neg_num = True

    # Checks for float number character '.'
    if '.' in num_str_upper:
        is_float_num = True

    # Checks that there is only one decimal point character in the string if number is a float
    if is_float_num and num_str_upper.count('.') > 1:
        return None

    # Checks for hexadecimal number characters '0X'
    if num_str_upper[0] == '0' and num_str_upper[1] == 'X':
        num_str_upper = num_str_upper[2:]
        is_hex_num = True

    num_str_len = len(num_str_upper) - 1
    # Calls conv_float helper function if number is a float
    if is_float_num:
        return conv_float(num_str_upper, return_num, is_neg_num)

    # Calls conv_hex helper function if number is a hexadecimal
    if is_hex_num:
        return conv_hex(num_str_upper, num_str_len, return_num, is_neg_num)

    # Calls conv_int helper function if number is an integer
    return conv_int(num_str_upper, num_str_len, return_num, is_neg_num)


def conv_int(num_str, num_str_len, ret_num, is_neg_num):
    """
    This helper function takes in an integer as a string and converts it into an integer
    Returns the integer if input string was valid, otherwise 'None' is returned
    """

    # Iterates through each digit of the input string
    for digit in num_str:
        cur_digit = ord(digit) - 48
        # Checks if digit is within bounds
        if cur_digit < 0 or cur_digit > 9:
            return None
        if num_str_len > 0:
            cur_digit *= (10 ** num_str_len)
            ret_num += cur_digit
            num_str_len -= 1
        else:
            ret_num += cur_digit

    # Multiplies return number by -1 if is_neg_num is True
    if is_neg_num:
        ret_num *= -1

    return ret_num


def conv_float(num_str, ret_num, is_neg_num):
    """
    This helper function takes in a float number as a string and converts it into a float number
    Returns the float number if input string was valid, otherwise 'None' is returned
    """

    # Splits input string at decimal point
    split_num_str = num_str.split('.')
    num_str_len = len(split_num_str[0]) - 1
    count = 1

    # Calls conv_int function to convert whole numbers of input string
    ret_num += conv_int(split_num_str[0], num_str_len, ret_num, is_neg_num)
    if ret_num < 0:
        ret_num *= -1

    # Iterates through fraction values of the input string
    for digit in split_num_str[1]:
        cur_digit = ord(digit) - 48
        if cur_digit < 0 or cur_digit > 9:
            return None
        cur_digit /= (10 ** count)
        ret_num += cur_digit
        count += 1

    # Multiplies return number by -1 if is_neg_num is True
    if is_neg_num:
        ret_num *= -1

    return ret_num / 1


def conv_hex(num_str_upper, num_str_len, ret_num, is_neg_num):
    """
    This helper function takes in a hexadecimal number as a string and converts it into an integer
    Returns the integer if input string was valid, otherwise 'None' is returned
    """

    # Iterates through hexadecimal numbers of the input string
    for digit in num_str_upper:
        cur_digit = ord(digit)

        # Checks if input character is within 0-9 bounds
        if 47 < cur_digit < 58:
            cur_digit -= 48

        # Checks if input character is within A-F bounds
        elif 64 < cur_digit < 71:
            cur_digit -= 55
        else:
            return None

        cur_digit *= (16 ** num_str_len)
        ret_num += cur_digit
        num_str_len -= 1

    # Multiplies return number by -1 if is_neg_num is True
    if is_neg_num:
        ret_num *= -1
    return ret_num


def my_datetime(num_sec):

    if num_sec < 86400:
        date = '01-01-1970'
        return date

    month = 1
    day = 1
    year = 1970
    months = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    num_sec -= 86400

    while num_sec >= 0:
        day += 1

        if months[month] < day:
            if month == 12:
                month = 1
                year += 1

                if year % 4 == 0:
                    if year % 100 == 0 and year % 400 != 0:
                        months[2] = 28
                    else:
                        months[2] = 29
                else:
                    months[2] = 28

            else:
                month += 1
            day = 1

        num_sec -= 86400

    if day < 10:
        day = f'0{day}'
    else:
        day = f'{day}'

    if month < 10:
        month = f'0{month}'
    else:
        month = f'{month}'

    year = f'{year}'

    date = month + '-' + day + '-' + year
    return date


def conv_endian(num, endian='big'):
    return_str = ''
    counter = 0
    negative = False
    if num < 0:
        negative = True
    num = abs(num)
    while num > 0:
        remainder = num % 16
        num = num // 16
        counter += 1
        if remainder == 10:
            remainder_str = 'A'
        elif remainder == 11:
            remainder_str = 'B'
        elif remainder == 12:
            remainder_str = 'C'
        elif remainder == 13:
            remainder_str = 'D'
        elif remainder == 14:
            remainder_str = 'E'
        elif remainder == 15:
            remainder_str = 'F'
        else:
            remainder_str = str(remainder)
        return_str = remainder_str + return_str

        if counter == 2 and num > 0:
            counter = 0
            return_str = ' ' + return_str

    if len(return_str) % 2 == 1:
        return_str = '0' + return_str

    if endian == 'big':
        if negative:
            return_str = '-' + return_str
        return return_str

    # ------------------------------------------------------------------------------------------------

    elif endian == 'little':
        little_return = ""
        temp = ""
        counter = 0
        for element in return_str:
            counter += 1
            if counter != 3:
                temp += element
            else:
                little_return = temp + little_return
                temp = ""
                counter = 0

        if len(little_return) > 2:
            little_return = return_str[len(return_str) - 2] + return_str[len(return_str) - 1] + little_return

        little_return_2 = ""

        counter_2 = 0

        for element in little_return:
            if counter_2 == 1:
                little_return_2 = little_return_2 + element + ' '
                counter_2 = 0
            else:
                little_return_2 = little_return_2 + element
                counter_2 += 1

        if negative:
            little_return_2 = '-' + little_return_2
        return little_return_2

    else:
        return None
