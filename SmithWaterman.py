## Author: Indranil Ghosh, Jadavpur University, Physics Department

# Smith-Waterman Algorithm
# For local sequence alignment

import numpy as np
import pandas as pd

def s(x, y): return 5 if x==y else -3 #s is an example of substitution matrix
W=4 #W is the linear gap penalty

def score(x, y):
        S=0
        for i in range(len(x)):
                if x[i]=="-" or y[i]=="-":S-=W
                else:
                        S+=s(x[i], y[i])
        return(S)

A="TGTTACGG"
B="GGTTGACTA"

##A="CGTGAATTCAT"
##B="GACTTAC"

def SW(A, B):
        a="-"+A
        b="-"+B
        row=len(b)
        col=len(a)
        F=np.array([[0]*col]*row)

        for i in range(1, row):
                for j in range(1, col): F[i, j]=max([F[i-1, j-1]+s(b[i], a[j]), F[i-1, j]-W, F[i, j-1]-W, 0])
        print(F)
        #l, m=np.unravel_index(F.argmax(), F.shape)
        p=np.where(F==F.max())
        x=p[0]
        y=p[1]
        l=[]
        for i in range(len(x)):l+=[[x[i], y[i]],]

        L=[]
        S=[]
        
        # To find the final alignment
        X="" # for row string
        Y="" # for column string
        for I in range(len(l)):
                i=l[I][0]
                j=l[I][1]
                while F[i, j]>0:
                        if i>0 and j>0 and F[i,j]==F[i-1, j-1]+s(b[i], a[j]):
                                X=b[i]+X
                                Y=a[j]+Y
                                i-=1
                                j-=1
                        elif i>0 and F[i,j]==F[i-1, j]-W:
                                X=b[i]+X
                                Y="-"+Y
                                i-=1
                        else:
                                X="-"+X
                                Y=a[j]+Y
                                j-=1
                p=pd.DataFrame(np.array(([Y, X])), columns=["Results"])
                L+=[[X, Y], ]
                S+=[score(X, Y),]
                print(p)
                X=""
                Y=""
        Ind=S.index(max(S))
        r=L[Ind]
        return pd.DataFrame([max(S), r[0], r[1]], columns=["Results"])
print(SW(A,B))