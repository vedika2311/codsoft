import string
import random


length = int(input("How many characters do you want in your password? "))

random_char = ""
random_char += string.ascii_letters
random_char += string.digits
random_char += string.punctuation

password = []

for i in range(length):
    # generate result from random_char string
    result = random.choice(random_char)

    # appending a result to password
    password.append(result)

print("The generate password is : " + "".join(password))
