# Expression contains redundant bracket or not

def checkRedundancy(exp):
    stack = []
    for char in exp:
        
        # if closing bracket is encountered
        # 1. if top of stack is '(' then the exp has redundant brackets
        # 2. if we did not find any operator before the '(' then the exp has redundant expression

        if char == ')':
            flag = True
            top = stack.pop()

            while top != '(':
                if top in ['*', '/', '+', '-']:
                    flag = False
                
                top = stack.pop()
            
            if flag:
                return True
        else:
            stack.append(char)
    return False

exp = "(a+b)"

if checkRedundancy(exp):
    print("Redundancy")
else:
    print("No redundancy")