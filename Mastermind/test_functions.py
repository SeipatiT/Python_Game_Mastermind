import unittest
import mastermind
from mastermind import create_code, get_answer_input, \
    take_turn, check_correctness, run_game
from unittest.mock import patch
from io import StringIO
from test_base import captured_io


class Testcode(unittest.TestCase):
    def test_code_is_list(self):
        '''This will test that create_code creates a list with 
        integers that are within the range of 1-8. It will loop 100 times.'''
        for _ in range(1,100):
            the_range = range(1,8)
            list_correct_range = []
            in_range = [True, False]
            for x in create_code():
                if x in the_range:
                    list_correct_range.append("yes")
                else:
                    list_correct_range.append("no")
            if list_correct_range == ["Yes", "Yes", "Yes", "Yes"]:
                in_range = in_range[1] 
                self.assertTrue(in_range)
            self.assertEqual(isinstance(create_code(), list), True)
            pass
        

    def test_check_correctness(self):
        '''This will test that check_correctness returns either True of False'''
        self.assertTrue(check_correctness(10, 4))
        for x in range(0,3):
            self.assertFalse(check_correctness(8, x))
        pass
    

    @patch("sys.stdin", StringIO("111\n111a\n12345\n1234\n"))
    def test_compare(self):
        '''This will test that the user's input adheres to the set conditions. 
        If the input is less than 4, it will loop again (ask for input). 
        The same is true for all other tests.'''
        self.assertEqual(get_answer_input(), '1234')
        pass
        
     
    def test__show_correct_answer(self):
        '''This is to check that the code shows the correct answer.'''
        with captured_io(StringIO('1234\n')) as (out,err):
            mastermind.show_code('1234')
        output = out.getvalue().strip()
        self.assertEqual('The code was: 1234', output)
        pass


    @patch("sys.stdin", StringIO("1234\n")) 
    def test_take_turn(self):
        '''This will test that take_turn returns a tuple'''
        self.assertEqual(isinstance(take_turn(code=create_code()), tuple), True)
        pass  