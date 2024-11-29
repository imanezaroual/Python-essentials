num=int(input("Enter number:"))
for m in range(1, num+1):
    if m %3==0 and m %5==0:
        print("fizzbuzz")
    elif m % 3==0:
        print("fizz")
    elif m %5==0 :
        print("buzz")
    else :
        print (m)
    

