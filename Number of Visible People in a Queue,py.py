def canSeePeople(height):
    n=len(height)
    answer=[0]*n
    stack=[]
    for i in range(n-1,-1,-1):
        count=0
        while stack and height[i]>stack[-1]:
            count+=1
            stack.pop()

        if stack:
            count+=1

        answer[i]=count
        stack.append(height[i])
    return answer
height = [10,6,8,5,11,9]
print(canSeePeople(height))
