###ALG 1, Approximation Method
import math

print("Algorithm 1: Approximation Algorithm")

def approxAlg(xnull, tol):
    iter = 0
    diff = xnull
    x = xnull

    print("\n",iter, " : ", x)

    while(diff >= tol):
        
        iter+=1
        y = x
        x = (x/2)+(1/x)
        print("\n",iter, " : ", x)

        diff = abs(x-y)
    
    return print("\nConvergence after ", iter, " iterations")

approxAlg(1.5, .000001)

##alg 2 Bisection

print("\nAlgorithm 2: Bisection Method")

def bisectionAlg(tol, left, right, max):
    iter = 0
    def f(x):
        return x**3 + 4*x**2 - 10 

    while(abs(right-left) > tol and iter < max):
        iter += 1
        p = (left + right) / 2

        if((f(left) < 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0)):
            right = p
        else:
            left = p

    return print("\nWith a left bound of 1, right bound of 2, and a tolerance of 10^-3 we have",
        "\nconvergence after: ", iter, "iterations for this function.")
    
bisectionAlg(.001, 1, 2, 100)

print("\nAlgorithm 3: Fixed-Point Iteration function 1")

import math

##Alg 3 Fixed point

def fixedPointAlg(tol, approx, max):
    iter = 1
    while (iter < max):
        p = approx - approx*approx*approx - 4*(approx*approx) + 10
        ##p = math.sqrt(10 - approx**3)/2
        if math.isinf(p) or math.isnan(p):
            print("\nDiverges after ", iter, " iterations")
            break

        print(iter, " : ", p)

        if (abs(p - approx) < tol):
            print("\nSuccess after ", iter, " iterations")
            break

        iter += 1
        approx = p

    return

fixedPointAlg(.000001, 1.5, 50)

print("\nAlgorithm 3: Fixed-Point Iteration function 2")

import math

def fixedPointAlg(tol, approx, max):
    iter = 1
    while (iter < max):
        p = math.sqrt(10 - approx**3)/2
        if math.isinf(p) or math.isnan(p):
            print("\nDiverges after ", iter, " iterations")
            break

        print(iter, " : ", p)

        if (abs(p - approx) < tol):
            print("\nSuccess after ", iter, " iterations")
            break

        iter += 1
        approx = p

    return

fixedPointAlg(.000001, 1.5, 50)


print("\nAlgorithm 4: Newton-Raphsom Method")

##Alg 4 newton

def newton(f,df,x_null, error, max_iter = 100):

    xn = x_null
    iter = 1
    print(0, " : ", round(xn,10))

    while (iter < max_iter or iter == max_iter):
        fxn = f(xn)
        if abs(fxn) < error:
            return print("\nSuccess after", iter-1, "iterations.")

        Dfxn = df(xn)
        if Dfxn == 0:
            print("Error! Derivative is zero")
            return None

        xn = xn - fxn/Dfxn
        print(iter, " : ", round(xn, 10))
        iter += 1


    return iter

def f(x): 
    return math.cos(x) - x

def df(x):
    return -1*(math.sin(x)) - 1

root = newton(f,df,math.pi/4, 25*1e-17)

