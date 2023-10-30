# Lab 6: Version Control
# Arossa Adhikary & Lam Nguyen

def encode(password):
    # take in 8-digit password in string format containing only integers
    # encoder stores encoded password to new variable with each digit shifted up by three numbers

    # storing newly encoded password
    encoded_password = ""

    for item in password:
        # changing each string value to an integer
        item = int(item)
        # adding three to each item
        item += 3
        # selecting the ones place of each digit
        item = item % 10
        # changing value back to str for  final string formatting
        item = str(item)
        # appending each str value to final str
        encoded_password += item

    return encoded_password

def decode(password):
   pass

if __name__ == '__main__':

   password_encode = ""

   # printing menu until user choses to exit the program (option 3)
   while True:
       print("Menu")
       print("-------------")
       print("1. Encode")
       print("2. Decode")
       print("3. Quit")

       print()
       menu_input = int(input("Please enter an option: "))

       if menu_input == 1:
           password = print("Please enter your password to encode: ")

           print("Your password has been encoded and stored!")
       elif menu_input == 2:
           print(f"The encoded password is {encode(password)}, and the original password is {decode(password)}")
       elif menu_input == 3:
           break
       else:
           print("Please choose a menu option 1-3.\n")