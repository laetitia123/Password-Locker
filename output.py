#!/usr/bin/env python3.6
from credentials import Credentials
def create_credentials(pfacebook,pcanvas,ptwitter,pemail):
    '''
    Function to create a new contact
    '''
    new_credentials = Credentials(pfacebook,pcanvas,ptwitter,pemail)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save contact
    '''
    credentials.save_credentials()
def display_credentials():
    '''
    Function that returns all the saved contacts
    '''
    return Credentials.display_credentials()

def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Credentials")
                            print("-"*10)

                            print ("twitther....")
                            pfacebook = input()

                            print("Last name ...")
                            pcanvas= input()

                            print("Phone number ...")
                            ptwitter= input()

                            print("Email address ...")
                            email = input()


                            save_credentials(create_credentials(pfacebook,pcanvas,  ptwitter,email)) # create and save new contact.
                            print ('\n')
                            print(f"New Credentials{  pfacebook} {  pfacebook} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_credentials():
                                    print("Here is a list of all your cREDENTIALS")
                                    print('\n')

                                    for  credentials in display_credentials():
                                            print(f"{credentials.twitter} {credentials.facebook}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')
if __name__ == '__main__':

     main()