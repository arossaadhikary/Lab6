# Lab 6: Version Control
# Arossa Adhikary & Lam Nguyen


def encode(password):
  pass


def decode(password):
   pass


if __name__ == '__main__':


   password_encode = ""


   # printing menu
   while True:
       print("Menu")
       print("-------------")
       print("1. Encode")
       print("2. Encode")
       print("3. Quit")


       print()
       menu_input = int(input("Please enter an option: "))


       if menu_input == 1:
           password_to_encode = print("Please enter your password to encode: ")
           password_encoded = encode(password_to_encode)
           print("Your password has been encoded and stored!")
       elif menu_input == 2:
           print(f"The encoded password is {password_encoded}, and the original password is {password_to_encode}")
       elif menu_input == 3:
           break
       else:
           print("Please choose menu option 1-3.")







