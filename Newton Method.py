# MATH3601 Q6
# Luo Tianling; UID: 3035447178
# Solve x^4-x-10=0; smallest positive root: 1.8556
# Newton-Raphson method

# define function f(x)
def f(x):
    return x*x*x*x-x-10

def derivative(x):
    return 4*x*x*x-1

def newton(x_0):

    list=[]
    n=0
    N=100
    x_n=x_0

    while (f(x_n)>=0.0001 or f(x_n)<=-0.0001):
        x_n=x_n-f(x_n)/derivative(x_n)
        list.append(x_n)
        n=n+1
        if (n>=N):
            break

    print("The value of root is: ","%.4f"%x_n)
    print(list)

x_0=2
newton(x_0)

# The result is as follows
# The value of root is:  1.8556
# [1.870967741935484, 1.8557807016967116, 1.8555845610108843]
# Hence, 2 steps are needed to get the results with three decimal places.
