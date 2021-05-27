import random
items = {}

    
name = 'Tim'
code = str(random.randint(1000, 10000))
guess = "----"
hint = "****"
items[name] = [code, guess, hint]
        
print(items[name])

text =  "\n--------------------"
    #for pile, stones in enumerate(self._piles):
        #text += (f"\n{pile}: " + "O " * stones)
text += "\n--------------------"

fruit = {
    "banana": 1.00,
    "apple": 1.53,
    "kiwi": 2.00,
    "avocado": 3.23,
    "mango": 2.33,
    "pineapple": 1.44,
    "strawberries": 1.95,
    "melon": 2.34,
    "grapes": 0.98
}

for key, value in items.items():
    value = " , ".join(value)
    print("Player {}: {}".format(key, value))