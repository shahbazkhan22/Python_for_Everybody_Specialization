largest = 0
smallest = 0
x = True
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    else:
        try:
            n = int(num)
            if(x):
                smallest = n
                x = False
            if(n>largest):
                largest = n
            elif(n<smallest):
                smallest = n
        except ValueError:
            print('Invalid')    

print("Maximum is", largest)
print("Minimum is", smallest)