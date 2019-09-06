import unittest # Importing the unittest module
from user import User
from credentials import Credentials
import pyperclip
class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("laetitia123","herewego") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"laetitia123")
        self.assertEqual(self.new_user.password,"herewego")
    
class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("tttttTTTTDWEW12","Waranyanze126@ws","eaeaeeatgg","TTTFGGEHJGHSRTMN")
 # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.facebook,"tttttTTTTDWEW12")
        self.assertEqual(self.new_credentials.canvas,"Waranyanze126@ws")
        self.assertEqual(self.new_credentials.twitter,"eaeaeeatgg")
        self.assertEqual(self.new_credentials.email,"TTTFGGEHJGHSRTMN")

    def test_save_credentials(self):
        '''
        test_save_contact test case to test if the credentials object is saved into
         the contact list
        '''
        self.new_credentials.save_credentials() # saving the new contact
        self.assertEqual(len(Credentials.credentials_list),1)


if __name__ ==  '__main__':
    unittest.main()