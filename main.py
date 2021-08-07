import random
import string


len_password = int(input("Enter length of password:"))

upper = bool(input("Uppercase?: "))
print(f"UPPERCASE: {upper}")

lower = bool(input("Lowercase?: "))
print(f"lowercase: {lower}")

digits = bool(input("Digits?: "))
print(f"D1G175: {digits}")

punct = bool(input("Punctuation?: "))
print(f"punctuat!on {punct}")

ascii_lowercase = string.ascii_lowercase
ascii_uppercase = string.ascii_uppercase
digit_ = string.digits
punctuation = string.punctuation



password = ""

for x in range(len_password):
    list_rndm_pass = []
    #RNDM
    if lower:
        random_lowercase = random.choice(ascii_lowercase)
        list_rndm_pass.append(random_lowercase)
    if upper:
        random_uppercase = random.choice(ascii_uppercase)
        list_rndm_pass.append(random_uppercase)
    if digits:
        random_digits = random.choice(digit_)
        list_rndm_pass.append(random_digits)
    if punct:
       random_punctuation = random.choice(punctuation)
       list_rndm_pass.append(random_punctuation)

    # Shuffle deck
    random.shuffle(list_rndm_pass)
    # Connect
    random_password = ''.join(list_rndm_pass)

    # hey presto
    password = password + random_password


print(f"Your password: {password}")
