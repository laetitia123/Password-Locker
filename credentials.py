import pyperclip
import string
# import choice
class Credentials:
    """
    Class that generates new instances of credentials.
    """

    credentials_list = [] # Empty contact list

    def __init__(self,facebook,canvas,twitter,email):

      # docstring removed for simplicity

        self.facebook= facebook
        self.canvas = canvas
        self.twitter = twitter
        self.email= email
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the contact list
        '''
        return cls.credentials_list
    contact_list = [] # Empty contact list
 # Init method up here
    def save_credentials(self):

        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        Credentials.credentials_list.append(self)
      
    def delete_credentials(self):

        '''
        delete_contact method deletes a save credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)
    # @classmethod
    # def generate_password(cls):
    #     '''
    #     Method that generates a random alphanumeric password
    #     '''
    #     # Length of the generated password
    #     size = 8

    #     # Generate random alphanumeric 
    #     alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase

    #     # Create password
    #     password = ''.join( choice(alphanum) for num in range(size) )
        
    #     return password