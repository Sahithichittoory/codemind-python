p,c,b,m,cs=map(int,input().split())
s=(p+b+c+m+cs)/5;
if s>=90:
    print("Grade A")
elif s>=80:
    print("Grade B")
elif s>=70:
    print("Grade C")
elif s>=60:
    print("Grade D")
elif s>=40:
    print("Grade E")
else:
    print("Grade F")
    