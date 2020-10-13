# MATH3601 Q6
# Luo Tianling; UID: 3035447178
# Solve x^4-x-10=0; smallest positive root: 1.8556
# Bisection method

# define function f(x)
def f(x):
    return x*x*x*x-x-10
def bisection(a,b):

    list=[]
    if (f(a)*f(b)>=0):
        print("Cannot use bisection method in interval (", a,", ", b, ").")
        return
    c=a
    while ((b-a)>=0.0001):
        
        c=(a+b)/2
        list.append(c)

        if (f(c)==0.0):
            break

        if (f(c)*f(a)<0):
            b=c
        else:
            a=c
    
    print("The value of root is: ","%.4f"%c)
    print(list)

a=1
b=2
bisection(a,b)

# The result is as follows
# The value of root is:  1.8555
# [1.5, 1.75, 1.875, 1.8125, 1.84375, 1.859375, 1.8515625, 1.85546875, 1.857421875,
# 1.8564453125, 1.85595703125, 1.855712890625, 1.8555908203125, 1.85552978515625]
# Hence, 8 steps are needed to get the results with three decimal places.