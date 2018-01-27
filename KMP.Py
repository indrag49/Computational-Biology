## Author: Indranil Ghosh, Jadavpur University, Physics Department

#Knuth-Morris-Pratt Algorithm

S1="ACGTCCACGTACCCACA" #First String
S2="CCA" # Second String

# Table building algorithm

def Table(S):
        S=list(S)
        p=1
        c=0
        n=len(S)
        T=[0]*n
        T[0]=-1
        while p<n:
                if S[p]==S[c]:
                    T[p]=T[c]
                    p+=1
                    c+=1
                else:
                    T[p]=c
                    c=T[c]
                    while c>=0 and S[p]!=S[c]: c=T[c]
                    p+=1
                    c+=1
        return T

# Main Program
def KMP(S1, S2):
        T=Table(S2)
        P=[]
        i, j=0, 0
        n=len(S1)
        m=len(S2)
        while i+j<n:
                if S2[j]==S1[i+j]:
                        if j+1==m:
                                P+=[i, ]
                                i+=j-T[j]
                                j=T[j]
                        else:
                                j+=1
                else:
                        if T[j]>-1:
                                i+=j-T[j]
                                j=T[j]
                        else:
                                i+=j+1
                                j=0
        return(P)
                                                       
print(KMP(S1, S2))               

