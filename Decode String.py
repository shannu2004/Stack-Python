def decodeString(s):
    res=""
    num=0
    stack=[]
    for c in s:
        if c.isdigit():
            num=num*10+int(c)
        elif c=="[":
            stack.append(res)
            stack.append(num)
            res=""
            num=0
        elif c=="]":
            pnum=stack.pop()
            pstr=stack.pop()
            res=pstr+pnum*res
        else:
            res+=c
    return res
s = "3[a]2[bc]"
print(decodeString(s))
