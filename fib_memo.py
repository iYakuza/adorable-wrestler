val = input("How many numbers?\n")
val = int(val)
if val < 0:
    print("Now ", val, " is your number.\n", "Cheer up, be positive.")
elif val == 0:
    print("Now ", val, " is your number.\n", "Let there be light! Don't be nihilistic.")
else:
    print("Now ", val, " is your number.\n", "To finity and not beyond")

stiva = {}

def fib_memo(x):
    if x in stiva:
        return stiva[x]
    elif x <= 1:
        return x
    # if x == 1:
    #     value = 1
    # elif x == 2:
    #     value = 1
    # elif x > 2:
    else:
        numar_stiva = fib_memo(x-1) + fib_memo(x-2) 
        stiva[x] = numar_stiva
        return numar_stiva
for x in range (1, val):
    print(fib_memo(x))
    
