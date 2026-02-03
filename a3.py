dict1={"welcome":10, "to":20, "python":10, "programming": 10}
print(dict1)
x=int(input("enter the frequency value to be searched: " ) )
result=0
for key in dict1:
    if dict1[key] == x:
        result=result+1
print("the frequency of the value",x, "is",result)