import math

def f(x):
    return 6*pow(x,3)-12*pow(x,2)+3*x+5

a = -4
b = 4
e = 0.002

while(abs(b-a)>e):
    print("-------------------------------------------------------------------------------------------------")
    print("Startuem")
    t1 = 0.381966
    t2 = 1 - t1

    x1 = a + (b - a)*t1
    x2 = a + (b - a)*t2

    print("x1="+str(x1))
    print("x2="+str(x2))

    f1 = f(x1 - e)
    f2 = f(x2 - e)

    print("F1="+str(f1))
    print("F2="+str(f2))
    print("Start checking...")
    print("-------------------------------------------------------------------------------------------------")
    if(f1<f2):
        print("-------------------------------------------------------------------------------------------------")
        print("Uslovie f1<f2")
        b = x2
        x2 = x1
        f2 = f1
        x1 = a + (b - a)*t1
        f1 = f(x1)
        print("a="+str(a))
        print("b="+str(b))
        print("x1="+str(x1))
        print("x2="+str(x2))
        print("F1="+str(f1))
        print("F2="+str(f2))
        print("-------------------------------------------------------------------------------------------------")

    elif(f1>f2):
        print("-------------------------------------------------------------------------------------------------")
        print("Uslovie f1>f2")
        a=x1
        x1=x2
        f1=f2
        x2=a+(b-a)*t2
        f2=f(x2)
        print("a="+str(a))
        print("b="+str(b))
        print("x1="+str(x1))
        print("x2="+str(x2))
        print("F1="+str(f1))
        print("F2="+str(f2))
        print("-------------------------------------------------------------------------------------------------")
x = (a+b)/2
fm = f(x)
print("x="+str(x))
print("fm="+str(fm))   
