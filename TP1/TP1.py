#Variables
m = 80
g = 9.8
cdg = 0.31

deltaTime = 1

z = [0, 0, 1]
v0 = [50,0,0]
p0 = [0,0,4000]

#####
def multVect(v,c):
    v3 = [0,0,0]
    for coef in range(0,len(v3)-1):
        v3[coef] = v[coef]*c
    return v3

def multVecttoVect(v1,v2):
    v3 = [0,0,0]
    for coef in range(0,len(v3)-1):
        v3[coef] = v1[coef]*v2[coef]
    return v3

def divVect(v1,c):
    v3 = [0,0,0]
    for coef in range(0,len(v3)-1):
        v3[coef] = v1[coef]/c
    return v3

def sumVecttoVect(v1,v2):
    v3 = [0,0,0]
    for coef in range(0,len(v3)-1):
        v3[coef] = v1[coef]+v2[coef]
    return v3

def minusVecttoVect(v1,v2):
    v3 = [0,0,0]
    for coef in range(0,len(v3)-1):
        v3[coef] = v1[coef]-v2[coef]
    return v3

def sumCompVect(v):
    res = 0
    for val in v:
        res+=val
    return res


#####
def run():
    for val in range(0,15):
        runOnce(val)

def runOnce(t):
    print(v(t))
    print(p(t))
    print(a(t))

def v(t):
    if t==0:
        return v0
    time = t - deltaTime
    return sumVecttoVect(v(time),multVect(a(time),deltaTime))

def p(t):
    if t==0:
        return p0
    time = t - deltaTime
    return sumVecttoVect(p(time),multVect(v(time),deltaTime))

def a(t):
    return divVect(minusVecttoVect(multVect(z,-m*g),multVect(v(t),(cdg * sumCompVect(v(t))))),m)
