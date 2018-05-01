def perm(a, lo):
    hi=len(a)
    if(lo==hi):
        if(abs(a.index("B")-a.index("A")==1) and abs(a.index("C")-a.index("D")!=1)):
           print(a)
        else:
           for i in range(lo, hi):
               a[lo], a[i]=a[i], a[lo]
               perm(a, lo+1)
               a[lo], a[i]=a[i], a[lo]

def main():
    a = ['A', 'B', 'C', 'D', 'E']
    b=[]
    print(perm(a,0))
    
main()
             
           
                                                     
