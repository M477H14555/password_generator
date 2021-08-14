import random
import string


len_password = int(input("Enter length of password:"))
upper = bool(input("Uppercase?: "))
lower = bool(input("Lowercase?: "))
digits = bool(input("Digits?: "))
punct = bool(input("Punctuation?: "))


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

#print("--"*20)
#print(f"President Password")
list_president = []
for president, use in president_password.items():
        if use:
            list_president.append(president)
            #print(list_president, use)
#print(f"list president: {list_president}")
#print("--"*20)

password = ""
list_rndm_pass = []
for x in range(len_password):
    president = random.choice(list_president)

    #RNDM
    if president == "lower":
        random_char = random.choice(ascii_lowercase)
    elif president == "upper":
        random_char = random.choice(ascii_uppercase)
    elif president == "digits":
        random_char = random.choice(digit_)
    elif president == "punct":
       random_char = random.choice(punctuation)
    else:
        random_char = ""

    list_rndm_pass.append(random_char)
    #print(f"{list_rndm_pass}")

    # Shuffle deck
    random.shuffle(list_rndm_pass)
    #print(f"{list_rndm_pass}")

    # Connect
    # random_password = ''.join(list_rndm_pass)

    # hey presto
    password = password + random_char
    #print("--"*20)
password = "".join(list_rndm_pass)
print(f"Your password: {password}")
# DONE
