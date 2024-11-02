# Polish Notation : Prefix Notations
# Reverse Polish Notation : Postfix Notations

def evalRPN(tokens):
    stack=[]
    for op in tokens:
        if op=='+':
            a,b=stack.pop(),stack.pop()
            stack.append(b+a)
        elif op=='-':
            a,b=stack.pop(),stack.pop()
            stack.append(b-a)
        elif op=='*':
            a,b=stack.pop(),stack.pop()
            stack.append(b*a)
        elif op=='/':
            a,b=stack.pop(),stack.pop()
            stack.append(int(b/a))
        else:
            stack.append(int(op))
    return stack.pop()
tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))


            
