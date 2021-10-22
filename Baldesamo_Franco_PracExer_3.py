

  
    
class Stack:
    
    
    print("This Program will convert your input number to binary, octal or hexadecimal.\n")
    number = input("Enter Number: ")
    number = int(number)

    
    
    


    dec_to_bin = bin(number)
    dec_to_oct = oct(number)
    dec_to_hex = hex(number)

    #stack
    mystack=[]
    mystack.append(dec_to_bin)
    mystack.append(dec_to_oct)
    mystack.append(dec_to_hex)
    
     
    a = mystack.pop()
    print(a)

    a = mystack.pop()
    print(a)

    a = mystack.pop()
    print(a)

    



    
    

    
    


