#!/usr/bin/env python3.6
from credentials import Credentials
from user import User
def create_credentials(pfacebook,pcanvas,ptwitter,pemail):
    '''
    Function to create a new contact
    '''
    new_credentials = Credentials(pfacebook,pcanvas,ptwitter,pemail)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()
def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()
def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()

def check_existing_credentials(name):
    '''
    Function that check if an account exists with that name and return a Boolean
    '''
    return Credentials.credentials_exist(name)  
# def create_generated_password():
#     '''
#     Function that generates a password for the user 
#     Args:
#         name : the name of the account
#     '''
#     password = Credentials.generate_password()

#     return password


#     ........................................................USER..............................
def create_user(user_name,password):
    '''
    Function to create a new account
    '''
    new_user = User(user_name,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()    

def del_user(user):
    '''
    Function to delete a account
    '''
    user.delete_user()    


def find_user(name):
    '''
    Function that finds a account by nane and returns the account
    '''
    return User.find_by_name(name)    

def check_existing_user(name):
    '''
    Function that check if an account exists with that name and return a Boolean
    '''
    return User.user_exist(name)    

def display_user():
    '''
    Function that returns all the saved accounts
    '''
    return User.display_user()  
def main():

    print("Hello Welcome to your Pass Word Locker. What is your name?")
    user_name = input()
    print(f"Hello {user_name}, sign up to Pass Word Locker to create an account.")
    print('\n')
    while True:
        print("Use these known short codes to operate :\n SU -> SIGN UP.\n DA -> Display your account.\n LN ->LOGIN.\n ex ->exit Pass Word Locker. ")
        short_code = input().lower()
        if short_code == 'su':
            print("Create a Pass Word Locker Account")
            print("_"*100)
            user_name= input('Account name:')
            print ('\n')
            password = input('User name:')
            print ('\n')
           
            save_user(create_user(user_name,password)) 
            print ('\n')
            print(f"A New {user_name} Account with the user name  {user_name} has been created.")
            print(f"You can now login to your {user_name} account using your password.")
            print ('\n')
        elif short_code == 'da':
             if display_user():
                 print("Here is your account and your details")
                 print('\n')
                 for user in display_user():
                     print(f"Account name:{user.password}  User name: {user.user_name} ")
                     print('\n')
             else:
                 print('\n')
                 print("You dont seem to have created an account.Sign up to create a new account.")
                 print('\n')
        elif short_code == 'ln':
            print("Enter your password to login.")
            search_user = input()
            if check_existing_user(search_user):
                search_cred = find_user(search_user)
                print("\033[1;32;1m   \n")
                print(f"You are now logged in to your {user_name} account")
                print("\033[1;37;1m   \n")
#     handle = open("text-write.txt", "w+")  
#     handle.write("Hello Moringa")  
#     print("Hello Welcome to your credentials list. What is your name?")
#     user_name = input()

#     print(f"Hello {user_name}. what would you like to do?")
#     print('\n')

                while True:
                    print("Use these short codes : cc - create a new contact, dc - display contacts, fc -delete credentials, ex -exit the contact list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("please type your corresponding Credentials")
                            print("-"*10)

                            print ("twitther password")
                            pfacebook = input()

                            print("canvas password")
                            pcanvas= input()

                            print("twitter password")
                            ptwitter= input()

                            print("Email password")
                            email = input()


                            save_credentials(create_credentials(pfacebook,pcanvas,  ptwitter,email)) # create and save new contact.
                            print ('\n')
                            print(f"New Credentials {  pfacebook} ")
                            print ('\n')
                            print(f"New Credentials{ pcanvas} ")
                            print ('\n')
                            print(f"New Credentials{  ptwitter}" )
                            print ('\n')
                            print(f"New Credentials{  email}")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_credentials():
                                    print("Here is a list of all your CREDENTIALS")
                                    print('\n')

                                    for  credentials in display_credentials():
                                            print(f"{credentials.twitter} {credentials.facebook}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any credentials saved yet")
                                    print('\n')
                    elif short_code == 'fc':     
                              for  credentials in display_credentials():
                                      
                                     credentials. delete_credentials()
                                     print("deleted" )
#     handle.close()                             
if __name__ == '__main__':

   main()
