a = int(input("Enter The Number Of Lines you want to Add; "))
b = bool(int(input("Enter '0' for false and '1' for True; ")))

def star(a, b):
    if b==(False):
        for i in range(a):
            a = a-1
            print(a*"*")

    if b==(True):
        for i in range(a):
            print(i*"*")

star(a, b)
