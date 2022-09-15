n = int(input())
modify = input()

number1 = []
number2 = []
stack = []
    
for i in range(len(modify)):
    if modify[i] == "+":
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num1 + num2)
        
    elif modify[i] == "-":
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num2 - num1)
        
    elif modify[i] == "*":
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num1 * num2)
        
    elif modify[i] == "/":
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num2 / num1)
        
    else:
        if len(number1) == 0:
            temp = int(input())
            number1.append(modify[i])
            number2.append(temp)
            stack.append(temp)
        else:
            if modify[i] in number1:
                stack.append(number2[number1.index(modify[i])])
            else:
                temp = int(input())
                number1.append(modify[i])
                number2.append(temp)
                stack.append(temp)
        
print(round(stack[0], 2))
