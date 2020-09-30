#Password Generator
import random
import string

uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
punctuation = string.punctuation
password_list = {1: uppercase_letters,
                 2: lowercase_letters,
                 3: digits,
                 4: punctuation}

while True:
    try:
        password_length = int(
            input("Enter the length of the password you want to generate: "))
        print('\n')
        if password_length <= 0:
            print("The Password length s negative or null as password length")
        elif password_length > 0:
            break
    except ValueError:
        print("Please enter a proper integer for your password length ")

print("\n".join(["MENU", "1: Uppercase Letters",
                 "2: Lowercase Letters", "3: Numerics", "4: Punctuations"]))

choice = (input("Enter you choice (For Ex: 124) : "))
choice_list = list(choice)
choice_list = list(map(int, choice_list))


new_character_list = []
for i in choice_list:
    new_character_list.extend(password_list.get(i))

random.shuffle(new_character_list)

print("Your password is: ", end=" ")
print("".join(new_character_list[0:password_length]))
