b=float(input())
if b<=10000:
    da=b*0.8
    hra=b*0.2
elif b<=20000:
    da=b*0.9
    hra=b*0.25
elif b>20000:
    da=b*0.95
    hra=b*0.3
g=b+hra+da
print(f"{g:.2f}")