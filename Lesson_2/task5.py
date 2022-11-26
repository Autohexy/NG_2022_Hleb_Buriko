myarr=[]
for number in range(1, 10):
    myarr.append(int(input("Enter a number: ")))
max=max(myarr)
min=min(myarr)
sum=0
for number in myarr:
    if number !=max and number !=min:
        sum+=number
print("Sum of numbers",sum,"\n","Min", min,"\n", "Max", max,)
        
