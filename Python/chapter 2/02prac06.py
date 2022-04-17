#sqaure of single number
a = input("enter the number :- ")
a = int(a)
square = a*a
print("the sqaure of the number is", square)
#sqaure of multiple numbers
def square(b):
    return b * b

for i in range(9):
    print(f"the square of {i} is {square(i)}")