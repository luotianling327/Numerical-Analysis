# MATH3601 Q6
# Luo Tianling; UID: 3035447178
# Solve x^4-x-10=0; smallest positive root: 1.8556
# Secant method

# define function f(x)
def f(x):
    return x*x*x*x-x-10

def d(x_n1,x_n2):
    return (x_n2-x_n1)/(f(x_n2)-f(x_n1))

def secant(x_0, x_1):

    list=[]
    n=0
    N=100
    x_n1=x_0
    x_n2=x_1
    x_n3=x_n2-d(x_n1,x_n2)*f(x_n2)
    list.append(x_n3)

    while (f(x_n3)>=0.0001 or f(x_n3)<=-0.0001):
        
        x_n1=x_n3
        x_n3=x_n3-d(x_n2,x_n3)*f(x_n3)
        list.append(x_n3)
        x_n2=x_n1
        n=n+1
        if (n>=N):
            break

    print("The value of root is: ","%.4f"%x_n3)
    print(list)

x_0=1
x_1=2
secant(x_0,x_1)

# The result is as follows
# The value of root is:  1.8556
# [1.7142857142857144, 1.8385312463222314, 1.8577757949191447, 1.8555528651416895, 1.8555844703303477]
# Hence, 4 steps are needed to get the results with three decimal places.
