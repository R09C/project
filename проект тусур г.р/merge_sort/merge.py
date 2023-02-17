def merge(n1,n2):
    i=0
    j=0
    len1=len(n1)
    len2=len(n2)
    n=[]
    while i<len1 and j<len2:
        if n1[i]<=n2[j]:
            n.append(n1[i])
            i+=1
        else:
            n.append(n2[j])
            j+=1
    n=n+n1[i:len1]
    n=n+n2[j:len2]
    return(n)

if __name__=="__main__":
    n1=[1,3,6,7,10,11,32,34]
    n2=[0,0,16,16,17,22]
    print(merge(n1,n2))
            
            

