def FizzBuzz(r):
    r=int(r)
    for i in range(1,r):
        if(i%3==0 and i%5==0):
            print(str(i)+" = FizzBuzz")
        
        else:
            if(i%5==0):
                print(str(i)+" = Buzz")
            else:
                if(i%3==0):
                    print(str(i)+" = Fizz")
                else:
                    print(str(i))
            