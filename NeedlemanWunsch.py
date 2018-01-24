## Author: Indranil Ghosh, Jadavpur University, Physics Department

# Needleman-Wunsch algorithm
        
import numpy as np
import pandas as pd
gap=2
def s(x, y): return 1 if x==y else -1 # This is the match-mismatch function

A="AGT"
B="AAGC"

def NW(A, B, gap):
        a="-"+A
        b="-"+B
        row=len(b)
        col=len(a)
        F=np.array([[0]*col]*row)
        F[0, 0]=0
        for i in range(1, row): F[i, 0]=F[i-1, 0]-gap
        for j in range(1, col): F[0, j]=F[0, j-1]-gap
        for i in range(1, row):
                for j in range(1, col):
                    F[i, j]=max([F[i-1, j]-gap, F[i, j-1]-gap, F[i-1, j-1]+s(b[i], a[j])])
        print(F)
        score=F[row-1, col-1] # score of the optimal alignment

        # To find the final alignment
        X="" # for row string
        Y="" # for column string
        i=row-1
        j=col-1
        while i>0 or j>0:
                if i>0 and j>0 and F[i,j]==F[i-1, j-1]+s(b[i], a[j]):
                        X=b[i]+X
                        Y=a[j]+Y
                        i-=1
                        j-=1
                elif i>0 and F[i,j]==F[i-1, j]-gap:
                        X=b[i]+X
                        Y="-"+Y
                        i-=1
                else:
                        X="-"+X
                        Y=a[j]+Y
                        j-=1
        p=pd.DataFrame(np.array(([score, Y, X])), columns=["Results"])
        return(p)
print(NW(A, B, gap))