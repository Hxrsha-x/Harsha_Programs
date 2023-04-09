#Python program to calculate lines/inches based on the input values D and L
import math
avg=[]
for i in range(5):
    d=float(input("Enter the value of D: "))
    l=float(input("Enter the value of L: "))
    x=l/d
    x=str(x)
    tan=""
    for i in range(6):
        if i>= len(x):
            tan+="0"
        else:
            tan+=x[i]
    tan=float(tan)
    #a=math.tan(math.radians(x))
    print("Tan is",tan)
    theta=math.degrees(math.atan(tan))
    tc=theta
    tc=int(round(tc,0))
    tc=str(tc)
    m=len(tc)
    theta=str(theta)
    t=""
    for i in range(5+m):
        t+=theta[i]
    t=float(t)
    print("Theta is",t)
    sin=math.sin(math.radians(t))
    sin=str(sin)
    s=""
    for i in range(6):
        s+=sin[i]
    s=float(s)
    print("Sin is",s)
    avg.append(str(s))
sum=0
for i in avg:
    sum+=float(i)
print("The average of sine is",sum/5)
sum=sum/5
sum=str(sum)
sf=""
for i in range(6):
    sf+=str(sum[i])
sf=float(sf)
print(sf)
o=int(input("Enter the order: "))
g=(sf*(10**5))/(o*2.3622)
print("The value of N is",g)
