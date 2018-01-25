## Author: Indranil Ghosh, Jadavpur University, Physics Department

# Rabin-Karp Algorithm

import pandas as pd
def Hash(S):
        a=0
        for i in S: a=((ord(i)+a)%101)*256
        return a/256

def RK(S, T):
        #S is the larger string and T is the pattern to be searched in S
        H=Hash(T)
        n=len(S)
        l=len(T)
        for i in range(n-l+1):
                s=Hash(S[i:i+l])
                if s==H:
                        if S[i:i+l]==T[:l]:
                                return pd.DataFrame([S, i*"-"+T+(n-(i+l))*"-"], columns=["Alignment"])
        return "No Alignment Found"
