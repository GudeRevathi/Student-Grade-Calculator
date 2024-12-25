score=[] 
n=int(input("enter number of subjects:"))
for i in range(n):
    n1=float(input("enter marks: "))
    score.append(n1) 
avg=sum(score)/len(score)

if avg>=90:
    print("grade A")
elif avg<90 and avg>=80:
    print("grade B") 
elif avg<80 and avg>=70:
    print("grade C") 
elif avg<70 and avg>=60:
    print("grade D")
else:
    print("Fail")