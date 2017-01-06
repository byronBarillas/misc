# The functions pertinent to Statistics are here:
import random

######----MEASURES OF CENTRAL LOCATION---------###############

## Arithmetic mean for a sample ######################
def Mean(L):
    x_bar = float(sum(L))/len(L)
    return x_bar

## Median of a sample ################################
def Median(L):
    L.sort()
    n = len(L)
    # Test to see if the length of L is an even number:
    even_b = (float(n)/2-n/2 == 0)
    if even_b:
        median= float(L[n/2]+L[n/2+1])/2
    else:
        median = L[n/2+1]
    return median
## Find the mode of discrete or categorical data
def Mode(L):
    L.sort()
    V = [L[0]]
    R = [0]
    a0 = L[0]
    for a in L:
        if a != a0:           
            V.append(a)
            R.append(1)
            a0 = a
        else:
            R[-1] = R[-1] + 1
    return [V,R]


######----MEASURES OF VARIABILITY---------###############



## Finds the histogram data for a set of continuous data set ##################
# This function organises the data into bins

def Hist_Data(L,NoOfBins):
    L.sort()
    R = NoOfBins*[0]
    V = NoOfBins*[0]
    Lrange = float(abs(L[0]-L[-1]))
    dx = Lrange/NoOfBins
    ## Give me upper bound for bins in Both V and R
    m = 1
    for i in range(len(R)):
        R[i] = m*dx+VEC[0]
        m = m + 1
    m = 1
    a0 = -100000
    for i in range(len(R)):
        c = 0     
        for b in L:
            if a0 < b <= R[i]:
                V[i]= V[i] + 1
        a0 = R[i]

    return [R,V]


## Finds the Range of the data
def Range(L):
    L.sort()
    return L[-1]-L[0]

## Finds the Variance of the data
def Variance_Smpl(L):
    n = len(L)
    SumLSqrd = 0
    for i in range(n):
        SumLSqrd = SumLSqrd + L[i]**2
    
    return (SumLSqrd - n*Mean(L)**2)/(n-1)
    
## Finds Standard Deviation of a sample
def Standard_Deviation_Smpl(L):
    return Variance_Smpl(L)**.5

## Finds Coefficient of variation of a sample
def Coefficient_of_Variation(L):
    return Standard_Deviation_Smpl(L)/Mean(L)
