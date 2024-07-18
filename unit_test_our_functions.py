import unittest

import our_functions

class test_is_valid_date(unittest.TestCase):
    def test_correct_date_format(self):
        date_str = "2023-01-01"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, True)

    def test_incorrect_date_format(self):
        date_str = "03-12-2023"
        res = our_functions.is_valid_date("date_str")
        self.assertEqual(res, False)

    def test_lower_than_range(self):
        date_str = "0999-12-13"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)
    
    def test_upper_than_range(self):
        date_str = "0999-12-13"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)

    def test_month_zero(self):
        date_str ="2013-00-12"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res,False)

    def test_month_Thirdteen(self):
        date_str ="2013-13-12"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res,False)

    def test_leap_year_is_true(self):
        date_str = "2024-02-14"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res,True)

    def test_leap_year_is_not_true(self):
        date_str = "2013-02-14"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res,True)
    
    def test_day_of_month(self):
        date_str = "2013-02-00"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res,False)

    def test_exception(self):
        date_str = "aaaaaaaaaa"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res,False)


class test_is_valid_username(unittest.TestCase):
    def test_username_more_than_min(self):
        username_str = "myname"
        min_username_chars = 5
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, True)

    def test_username_equal_min(self):
        username_str = "myname"
        min_username_chars = 6
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, True)

    def test_minlen_below_1(self):
        username_str = ""
        min_username_chars = 0  
        with self.assertRaises(ValueError) as context:
            our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(str(context.exception), "minlen must be at least 1")

    def test_name_minlen(self):
        username_str = "dream"
        min_username_chars = 6
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, False)
    
    def test_not_match(self):
        username_str = "dr@am"
        min_username_chars = 5
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, False)

    def test_not_str(self):
        username_str = "1dsed"
        min_username_chars = 5
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, False)
    
    # def test_not_string(self):
    #     username_str = 11234
    #     min_username_chars = 5
    #     res = our_functions.is_valid_username(username_str, min_username_chars)
    #     self.assertEqual(res, False)

    
    def test_not_string(self):
        username_not_str = 11234  # ไม่ใช่สตริง จะทำให้เกิด TypeError
        min_username_chars = 5
        with self.assertRaises(TypeError) as context:
            our_functions.is_valid_username(username_not_str, min_username_chars)
        self.assertEqual(str(context.exception), "username must be a string")



if __name__ == "__main__":
    unittest.main()