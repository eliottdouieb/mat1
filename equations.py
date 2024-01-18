import pandas as pd
import numpy as np

def exponent(x):
    n=1.0
    b=1.0
    a=1.0
    c=1.0
    d=1.0
    e=1.0
    while (n<=200.0):
        while(b>0.0):
            a=a*b
            b=b-1.0
        while(c>0):
            d=d*x
            c=c-1.0
        e=e+(d/a)
        n=n+1.0
        b=n
        a=1.0
        c=n
        d=1.0
    return e

def Ln(x):
    if x<=0:
        return 0
    else:
        x=float(x)
        yn=x-1.0
        yn=float(yn)
        while(True):
            yn1=yn+2.0*((x-exponent(yn))/(x+exponent(yn)))
            z=yn-yn1
            if z<0:
                z=z*(-1)
            if z>0.001:
                yn=yn1
                continue
            else :
                break
        return yn1


def XtimesY(x,y):
    if x<=0.0 :
        return 0.0
    else :
        a=exponent(y*Ln(x))
        return a

def sqrt(x,y):
    if x<=0.0:
        return 0.0
    else:
        return XtimesY(y,(1/x))

def calculate(x):
    if x<= 0.0:
        return 0.0
    else :
        return (exponent(x)*XtimesY(7,x)*XtimesY(x,(-1))*sqrt(x,x))
    

def sum(L) : 

    S = 0 
    for i in L : 
        S = S+i 
    return S


