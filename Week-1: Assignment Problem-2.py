lsstring=[]
n=int(input("Enter number of strings to be added: "))

for i in range(0,n):
    s=input("---> ")
    lsstring.append(s)


for i in range(0,n):
    for j in range (0,n-1-i):
        if len(lsstring[j])>len(lsstring[j+1]):
            temp=lsstring[j]
            lsstring[j]=lsstring[j+1]
            lsstring[j+1]=temp

print(lsstring)
