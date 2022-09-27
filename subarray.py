def verif(s, d, m):
    temp=[]
    finale=[]
    maxt=0
    for i in s:
        temp.append(i)
        if len(temp)==m and sum(temp)==d and temp not in finale:
            finale.append(temp)
            maxt+=1
    return maxt
            
def birthday(s, d, m):
    # Write your code here
    nbre=0
    for i in range(len(s)):
        tab=s[i:]
        nbre+=verif(tab, d, m)
    return nbre
