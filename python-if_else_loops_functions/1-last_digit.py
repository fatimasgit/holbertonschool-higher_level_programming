import random
number = random.randint(-10000, 10000)

last_digit = int(str(number)[-1])
def n_last_digit():
 if number < 0:
    last_digit = last_digit * -1
 else: 
    last_digit = last_digit

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and it is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and it is 0")
elif last_digit != 0 & last_digit < 6:
    print(f"Last digit of {number} is {last_digit} and and is less than 6 and not 0")
