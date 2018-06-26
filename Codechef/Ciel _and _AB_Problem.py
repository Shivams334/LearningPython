#Problem statement
print("https://www.codechef.com/problems/CIELAB/")

#Solution
number1,number2=map(int,input().split())
ans=number1-number2
if answer%10==9:
    print(answer-1)
else:
    print(answer+1)
