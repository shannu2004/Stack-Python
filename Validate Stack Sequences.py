def validateStackSequences(pushed, popped):
    stack=[]
    j=0
    for x in pushed:
        stack.append(x)
        while stack and stack[-1] == popped[j]:
            stack.pop()
            j+=1
    return stack == []
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(validateStackSequences(pushed, popped))
pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
print(validateStackSequences(pushed, popped))


#TC = O(N)
#SC = O(N)
