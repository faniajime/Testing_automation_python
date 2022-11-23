import random
import string
def get_random_userAccount(length):
    letters = string.ascii_lowercase
    numbers = random.randint(1, 100)
    username = ''.join(random.choice(letters) for i in range(length))
    password = '$'.join(random.choice(letters) for i in range(length))+str(numbers)
    return "user"+username, password
