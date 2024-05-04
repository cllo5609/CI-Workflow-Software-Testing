import unittest
import random
import time
import calendar
from task import my_datetime
from task import conv_num
from task import conv_endian


class TestCase(unittest.TestCase):

    def test30(self):
        self.assertEqual((conv_endian(num=-954786, endian='small')), None)

    def test31(self):
        self.assertEqual((conv_endian(num=954786)), '0E 91 A2')

    def test32(self):
        self.assertEqual((conv_endian(num=-954786)), '-0E 91 A2')

    # Verifies if an empty string returns False
    def test_01(self):
        input_str = ''
        self.assertEqual(conv_num(input_str), None)

    # Verifies if an integer value returns False
    def test_02(self):
        input_str = 12345
        self.assertEqual(conv_num(input_str), None)

    # Verifies if an integer string returns True
    def test_03(self):
        input_str = '12345'
        return_val = 12345
        self.assertEqual(conv_num(input_str), return_val)

    # Verifies if a negative integer string returns True
    def test_04(self):
        input_str = '-12345'
        return_val = -12345
        self.assertEqual(conv_num(input_str), return_val)

    # Verifies if an integer string with two negative characters returns False
    def test_05(self):
        input_str = '-12-345'
        self.assertEqual(conv_num(input_str), None)

    # Verifies if a float number string returns True
    def test_06(self):
        input_str = '123.45'
        return_val = 123.45
        self.assertEqual(conv_num(input_str), return_val)

    # Verifies if a negative float number string returns True
    def test_07(self):
        input_str = '-123.45'
        return_val = -123.45
        self.assertEqual(conv_num(input_str), return_val)

    # Verifies if a float number returns False
    def test_08(self):
        input_str = 123.45
        self.assertEqual(conv_num(input_str), None)

    # Verifies if a float number string with two decimal place points returns False
    def test_09(self):
        input_str = '1.23.45'
        self.assertEqual(conv_num(input_str), None)

    # Verifies if a float number string with no whole numbers returns True
    def test_10(self):
        input_str = '.45'
        return_val = 0.45
        self.assertEqual(conv_num(input_str), return_val)

    # Verifies if a float number string with no fractions returns True
    def test_11(self):
        input_str = '123.'
        return_val = 123.0
        self.assertEqual(conv_num(input_str), return_val)

    # Verifies if a valid hexadecimal number string returns True
    def test_12(self):
        input_str = '0xAD4'
        return_val = 2772
        self.assertEqual(conv_num(input_str), return_val)

    # Verifies if a valid hexadecimal number string with lowercase letters returns True
    def test_13(self):
        input_str = '0xad4'
        return_val = 2772
        self.assertEqual(conv_num(input_str), return_val)

    # Verifies if a hexadecimal number returns False
    def test_14(self):
        input_str = 0xAD4
        self.assertEqual(conv_num(input_str), None)

    # Verifies if an invalid hexadecimal number string returns False
    def test_15(self):
        input_str = '0xAZ4'
        self.assertEqual(conv_num(input_str), None)

    # Verifies if a hexadecimal number string without leading '0x' returns False
    def test_16(self):
        input_str = 'AD4'
        self.assertEqual(conv_num(input_str), None)

    # Verifies if a randomly generated integer string returns True
    def test_17(self):
        for _ in range(10000):
            rand_num_str = str(random.randint(0, 9999999999))
            self.assertTrue(conv_num(rand_num_str))

    # testing for 0 seconds
    def test_time_1(self):
        self.assertEqual(my_datetime(0), '01-01-1970', 'Dates are not equal')

    # testing for exactly one day
    def test_time_2(self):
        date = time.gmtime(86400)
        year, month, day = date[0], date[1], date[2]
        date = f'0{month}-0{day}-{year}'
        self.assertEqual(my_datetime(86400), date, 'Dates are not equal')

    # testing for 1 sec before new day
    def test_time_3(self):
        date = time.gmtime(86399)
        year, month, day = date[0], date[1], date[2]
        date = f'0{month}-0{day}-{year}'
        self.assertEqual(my_datetime(86399), date, 'Dates are not equal')

    # testing for one regular year
    def test_time_4(self):
        date = time.gmtime(31536000)
        year, month, day = date[0], date[1], date[2]
        date = f'0{month}-0{day}-{year}'
        self.assertEqual(my_datetime(31536000), date, 'Dates are not equal')

    # 1 sec before end of regular year and date without prepended 0's
    def test_time_5(self):
        date = time.gmtime(31535999)
        year, month, day = date[0], date[1], date[2]
        date = f'{month}-{day}-{year}'
        self.assertEqual(my_datetime(31535999), date, 'Dates are not equal')

    # change of month with 31 days
    def test_time_6(self):
        date = time.gmtime(2678400)
        year, month, day = date[0], date[1], date[2]
        date = f'0{month}-0{day}-{year}'
        self.assertEqual(my_datetime(2678400), date, 'Dates are not equal')

    # 1 second before change of month with 31 days, 0 prepended to month only
    def test_time_7(self):
        date = time.gmtime(2678399)
        year, month, day = date[0], date[1], date[2]
        date = f'0{month}-{day}-{year}'
        self.assertEqual(my_datetime(2678399), date, 'Dates are not equal')

    # 28 Feb - March
    def test_time_8(self):
        date = time.gmtime(5097600)
        year, month, day = date[0], date[1], date[2]
        date = f'0{month}-0{day}-{year}'
        self.assertEqual(my_datetime(5097600), date, 'Dates are not equal')

    # 1 second before 28 Feb - March
    def test_time_9(self):
        date = time.gmtime(5097599)
        year, month, day = date[0], date[1], date[2]
        date = f'0{month}-{day}-{year}'
        self.assertEqual(my_datetime(5097599), date, 'Dates are not equal')

    # end of 30 day month
    def test_time_10(self):
        date = time.gmtime(10368000)
        year, month, day = date[0], date[1], date[2]
        date = f'0{month}-0{day}-{year}'
        self.assertEqual(my_datetime(10368000), date, 'Dates are not equal')

    # 1 second before end of 30 day month
    def test_time_11(self):
        date = time.gmtime(10367999)
        year, month, day = date[0], date[1], date[2]
        date = f'0{month}-{day}-{year}'
        self.assertEqual(my_datetime(10367999), date, 'Dates are not equal')

    # Day only has prepended 0
    def test_time_12(self):
        date = time.gmtime(23587200)
        year, month, day = date[0], date[1], date[2]
        date = f'{month}-0{day}-{year}'
        self.assertEqual(my_datetime(23587200), date, 'Dates are not equal')

    # Extra day in leap year
    def test_time_13(self):
        date = time.gmtime(68169600)
        year, month, day = date[0], date[1], date[2]
        date = f'0{month}-{day}-{year}'
        self.assertEqual(my_datetime(68169600), date, 'Dates are not equal')

    # No leap year when year divisible by 100 but not 400
    def test_time_14(self):
        date_sec = calendar.timegm((2100, 3, 1, 0, 0, 0, 0, 1, 0))
        date = '03-01-2100'
        self.assertEqual(my_datetime(date_sec), date, 'Dates are not equal')

    # random tests
    def test_time_15(self):
        for _ in range(700):
            rand_sec = random.randint(0, 253402300799)
            date = time.gmtime(rand_sec)
            month = f'0{date[1]}' if date[1] < 10 else f'{date[1]}'
            day = f'0{date[2]}' if date[2] < 10 else f'{date[2]}'
            year = f'{date[0]}'
            self.assertEqual(
                my_datetime(rand_sec),
                month + '-' + day + '-' + year,
                'Dates are not equal'
            )


if __name__ == '__main__':
    unittest.main()
