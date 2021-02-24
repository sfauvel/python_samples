# coding: utf-8
import unittest
import json

class TestCalculator(unittest.TestCase):

    def test_json(self):
        data = '''{ 
            "XXX": 123
        }'''
        result = json.loads(data)
        self.assertEquals(123, result["XXX"])

    def test_json_multi_entry(self):
        data = '''{ 
            "XXX": 123,
            "XXX": 456,
            "XXX": 789
        }'''
        result = json.loads(data)
        self.assertEquals(789, result["XXX"])

    def parse_object_pairs_to_keep_first(self, pairs):        
        d = {}
        for k, v in pairs:
            if (not(k in d)):
                d[k] = v

        return d
        
    def test_json_multi_entry_with_hook_to_keep_first_key(self):
        data = '''{ 
            "XXX": 123,
            "XXX": 456,
            "XXX": 789
        }'''
        result = json.loads(data, object_pairs_hook=self.parse_object_pairs_to_keep_first)
        self.assertEquals(123, result["XXX"])

    def check_double_entry(self, pairs):
        d = {}
        for k, v in pairs:
            self.assertEquals(False, k in d)
            d[k] = v

        return d
        
    def test_json_check_double_entry_fail_with_multi_entry(self):
        data = '''{ 
            "XXX": {
                "YYY": {
                    "AAA": 123
                },
                "ZZZ": {
                    "AAA": 456,
                    "AAA": 789
                }
            }
           
        }'''
        exception_thrown = False
        try:
            json.loads(data, object_pairs_hook=self.check_double_entry)
        except:
            exception_thrown = True

        self.assertEquals(True, exception_thrown)

    def test_json_check_double_entry_pass_without_multi_entry(self):
        data = '''{ 
            "XXX": {
                "YYY": {
                    "AAA": 123
                },
                "ZZZ": {
                    "AAA": 456
                }
            }
           
        }'''
        result = json.loads(data, object_pairs_hook=self.check_double_entry)
        
        self.assertEquals(123, result["XXX"]["YYY"]["AAA"])
        self.assertEquals(456, result["XXX"]["ZZZ"]["AAA"])  

    
if __name__ == '__main__':
    unittest.main()
