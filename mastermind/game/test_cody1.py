import random
names = {}


name = 'Tim'
name2="bill"
code = str(random.randint(1000, 10000))
guess = "----"
hint = "****"
names[name] = [code, guess, hint]
        
#print(names[name])

text =  "\n--------------------"
    #for pile, stones in enumerate(self._piles):
        #text += (f"\n{pile}: " + "O " * stones)
text += "\n--------------------"

fruit = {
    "banana": '1234',
    "apple": '1234',
    "kiwi": '1234',
    "avocado": '1234',
    "mango": '1234',
    "pineapple": '1234',
    "strawberries": '1234',
    "melon": '1234',
    "grapes": '1234'
}

#for key, value in names.items():
    #value = " , ".join(value)
    #print("Player {}: {}".format(key, value))

#Splits the value
def split(variable):
    return list(variable)
guess = split(guess)
print(guess)
code = split(code)
print(code)
hint = split(hint)

n = str(input('Enter Number: '))
#guess = ["_"]*4
#correct = split(correct)
#print(correct)
for i in range(0, 4): 
  
    # checking for equality of digits
    if n[i] == code[i]:  

        # hence, the digit is stored in correct[].
        guess[i] = n[i]  


print(guess)

print( " ".join(guess))

print(" ".join(code))

print(" ".join(hint))


