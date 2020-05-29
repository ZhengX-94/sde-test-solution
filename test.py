import unittest
import json
import os


class TestStringMethods(unittest.TestCase):

    def test_sample(self):
        print("test_sample...")
        os.system(
            'python sde-test-solution.py sample_input_2.json sample_output_2.json')
        with open("./sample_output_2_expected.json", 'r') as file:
            expected_dict = json.load(file)
        with open("./sample_output_2.json", 'r') as file:
            output_dict = json.load(file)
        self.assertEqual(expected_dict, output_dict,
                         msg="the app cannot break the tie of tenor_diff")


if __name__ == '__main__':

    unittest.main()
