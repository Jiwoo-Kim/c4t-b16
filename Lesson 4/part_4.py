username = input("Enter your username: ")
email = input("Enter your email address: ")

while ("@" not in email) or ("." not in email):
    print("Your email address is not valid, please try again")
    email = input("Enter your email address: ")

password1 = input("Enter your password: ")

def notcontain_digit(password):
    for characters in password:
        if characters.isdigit() == True:
            return False
    return True

def notcontain_letter(something):
    for characters in something:
        if characters.isalpha() == True:
            return False
    return True


while (len(password1) < 8) or notcontain_digit(password1) == True or notcontain_letter(password1) == True:
    print("Please enter a password with at least 8 digits, including letters and numbers")
    password1 = input("Enter your password: ")

password2 = input("Re-enter your password: ")
 

while password1 != password2:
    print("Your password and your re-entered password do not match, please try again")
    password1 = input("Enter your password: ")
    while (len(password1) < 8) or notcontain_digit(password1) == True or notcontain_letter(password1) == True:
        print("Please enter a password with at least 8 digits, including letters and numbers")
        password1 = input("Enter your password: ")
    password2 = input("Re-enter your password: ")



user_info = {
    "Username" : username,
    "Email Address" : email,
    "Password" : password1
}