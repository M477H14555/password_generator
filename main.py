import random
import string


len_password = int(input("Enter length of password:"))

upper = bool(input("Uppercase?: "))

lower = bool(input("Lowercase?: "))

digits = bool(input("Digits?: "))

if digits == True:
    print("Minimum digits?: ")
    minid = int(input())
else:
    minid = 0

punct = bool(input("Punctuation?: "))

if punct == True:
    print("Minimum symbols?: ")
    minip = int(input())
else:
    minip = 0

# initial characters
ascii_lowercase = string.ascii_lowercase
ascii_uppercase = string.ascii_uppercase
digit_ = string.digits
punctuation = string.punctuation

president_password = {
    "upper": upper,
    "lower": lower,
    "digits": digits,
    "punct": punct
}

list_president = []
for president, use in president_password.items():
        if use:
            list_president.append(president)

password = ""
list_rndm_pass = []
count_lower = 0
count_upper = 0
count_digits = 0
count_punct = 0

for x in range(len_password):
    if count_digits < minid:
        president = "digits"
    elif count_punct < minip:
        president = "punct"
    else:
        president = random.choice(list_president)
    print(president)

    #RNDM
    if president == "lower":
        random_char = random.choice(ascii_lowercase)
    elif president == "upper":
        random_char = random.choice(ascii_uppercase)
    elif president == "digits":
        count_digits += 1
        random_char = random.choice(digit_)
    elif president == "punct":
        count_punct += 1
        random_char = random.choice(punctuation)
    else:
        random_char = ""

    list_rndm_pass.append(random_char)

    # Shuffle deck
    random.shuffle(list_rndm_pass)


    # hey presto
    password = password + random_char

password = "".join(list_rndm_pass)
print(f"Your password: {password}")
