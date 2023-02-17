def merge_sort(n):
    from merge_sort.merge import merge
    mid=len(n)//2
    n1=n[:mid]
    n2=n[mid:]
    if len(n1)>1:
        n1=merge_sort(n1)
    if len(n2)>1:
        n2=merge_sort(n2)
    return merge(n1,n2) 
    



if __name__=="__main__":
    n=[1,3,4,4,4,1]
    n=merge_sort(n)
    print(n)

