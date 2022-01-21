from binary_search import binary_search
from random import randint

random_list = list(set(randint(0, 1000) for _ in range(1000)))
print(binary_search(random_list, 123))
