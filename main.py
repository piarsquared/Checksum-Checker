import os
import sys
import time
import hashlib

logo = r"""

      __           __                 
 ____/ /  ___ ____/ /__ ___ __ ____ _ 
/ __/ _ \/ -_) __/  '_/(_-</ // /  ' \
\__/_//_/\__/\__/_/\_\/___/\_,_/_/_/_/
                                      

"""

print(logo)

main_menu = """Please select an option from below to continue.

1. Verify a file.
2. Get the checksum of a file.
0. Exit.
"""

print(main_menu)

def restart_prompt():
    choice = input("Would you like to run the program again? (y/n) > ")

    if choice == "y":
        clear_term()
        print(logo)
        print(main_menu)
    else:
        clear_term()
        print("Goodbye.")
        sys.exit()

def grab_checksum(file_path, mode, silent="n"):

      mode = mode.strip().lower() 

      try:

            with open(file_path, "rb") as f:
                  file_hash = hashlib.new(mode)
                  for chunk in iter(lambda: f.read(4096), b""):
                        file_hash.update(chunk)
    
      except FileNotFoundError:
            print("File not found.")
            return None


      try:

            clean_checksum = file_hash.hexdigest()

      except ValueError:
            print("Invalid hashing algorithm.")
            return None

      if silent == "n":
        print(f"\nYour checksum is: {clean_checksum}\n")
    
      return clean_checksum

def clear_term():
      os.system('cls' if os.name == 'nt' else 'clear')

def verify_match():

      file_path = input("Please enter the file path of the file > ").strip("'\"")

      mode = input("Please input the algorithm you would like (defaults to sha256) > ")

      checksum = input("Please paste the checksum > ").strip()

      if not mode:
            mode = "SHA256"

      user_checksum = grab_checksum(file_path, mode, "y")

      print("")

      if user_checksum.lower() == checksum.lower():
            print("Your checksum is valid.")
      else:
            print("These checksums do not match. File may be corrupted.")

      print("")

      restart_prompt()

def grabber():
      
      file_path = input("Please enter the file path of the file > ").strip("'\"")

      mode = input("Please input the alogithm you would like (defaults to sha256) > ")

      if not mode:
            mode = "SHA256"

      grab_checksum(file_path, mode)

      restart_prompt()

      if choice_two == "y":
            clear_term()
            print(logo)
            print(main_menu)
      elif choice_two == "n":
            clear_term()
            print("Goodbye.")
            sys.exit()

while True:

      user_choice = input("> ")

      try:
            user_choice = int(user_choice)
      except ValueError:
            pass

      match user_choice:

            case 1:
                  verify_match()
            case 2:
                  grabber()
            case 0:
                  print("Goodbye.")
                  time.sleep(1)
                  clear_term()
                  sys.exit()

            case _:
                  print("Invalid Option.")
                  time.sleep(1)
                  clear_term()
                  print(logo)
                  print(main_menu)
