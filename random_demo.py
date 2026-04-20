import random
import string


rand_int = random.randint(1, 10)

rand_float = random.random()

rand_uniform = random.uniform(5, 10)

fruits = ["apple", "banana", "mango", "orange"]
rand_choice = random.choice(fruits)


numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)

print("Random Integer (1-10):", rand_int)
print("Random Float (0-1):", rand_float)
print("Random Float (5-10):", rand_uniform)
print("Random Choice (Fruit):", rand_choice)
print("Shuffled List:", numbers)

