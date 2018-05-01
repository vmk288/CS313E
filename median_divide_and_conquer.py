def find_median(a,lo,hi,k):

    #finding the k-th number in the list a

    if lo>=hi:

        return

    #divide the list into two parts

    #the numbers at the left hand side of

    #the pivot are all less than the pviot

    pivot = a[lo]

    m = lo

    for i in range(lo,hi+1):

        if a[i]<pivot:

            m=m+1

            a[m],a[i]=a[i],a[m]

    a[lo],a[m]=a[m],a[lo]

    #if the pivot is the k-th one, then just return

    if m==k-1:

        return

    elif m<k-1:

    #if the index of the pivot is before the k-th number,

    #then recursively find the k-th number in the right part

        find_median(a,m+1,hi,k)

    else:

    #otherwise find the k-th number from the left part 

        find_median(a,0,m-1,k)

 

def main():

    a=[6,1,2,4,3,9,8]

    k=0

    med = 0

    if len(a)%2>0:

        #handling the case when the list has odd number of elements

        k=len(a)//2+1

        find_median(a,0,len(a)-1,k)

        med = a[k-1]

    else:

        #handling the case when the list has even number of elements

        k1 = len(a)//2

        find_median(a,0,len(a)-1,k1)

        med1 = a[k1-1]

        k2 = len(a)//2+1

        find_median(a,0,len(a)-1,k2)

        med2 = a[k2-1]

        med = (med1+med2)//2

 

    print(med)

 

main()
