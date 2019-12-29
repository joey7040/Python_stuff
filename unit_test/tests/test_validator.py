import unittest

from classes.validator import validator

class TestValidator(unittest.TestCase):
    
    def test_too_long(self):
        #Assume

        username = 'InvalidTooLong'

        #Action
        result = validator.user_is_valid(username)

        #Assert
        result = self.assertFalse(result)

    def test_has_space(self):
    #Assume

        username = 'Has Space'

        #Action
        result = validator.user_is_valid(username)

        #Assert
        result = self.assertFalse(result)

    def test_all_lower(self):
        #Assume

        username = 'lower'

        #Action
        result = validator.user_is_valid(username)

        #Assert
        result = self.assertFalse(result)

validator = validator()
    
if __name__ == '__main__':
    unittest.main()
