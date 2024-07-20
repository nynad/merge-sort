# merge sorting is when the list is divded and merged over and over again.
# 1. you divide the array in half.
# 2. you then divide those halves in half as well. 
# 3. keep repeating breaking into halves until you find the number you want to sort. 
# 4. when they're broken down into the smallest form, you can rearrange them based on their relationship (being greater or smaller than each other)
# 5. they MERGE into smaller arrays again. 
# 6. then, those arrays' contents are compared and merged to make a whole array.
# dividing and merging have different steps.

a=[2,9,3,5,7,4,8,6]

def merge(a,low,middle,high):
    list2=[]
    start1=low 
    start2=middle+1 
    while start1<=middle and start2<=high:
        if a[start1]<a[start2]:
            list2.append(a[start1])
            start1=start1+1 
        else:
            list2.append(a[start2])
            start2=start2+1 
        print(list2)
    while start1<=middle:
        list2.append(a[start1])
        start1=start1+1 
        print("Second")
        print(list2)
    while start2<=high:
        list2.append(a[start2])
        start2=start2+1 
        print("Third")
        print(list2)
    k=0 
    for i in range(low,high+1):
        a[i]=list2[k]
        k=k+1
# based on the condition (ascending) you "sort" and remerge the the singular items into lists. 
# the list is continiously added to until the starting index breaks the <= condition. it repeats until there are
# ONLY 2 big lists left.
# the secondary process is merging those 2 lists.
# the for loop continously sorts each item back into the original list, the secondary list dissolves 
# once all the sorting is done. list2 was temporary. 

    
def mergesort(a,start,end):
    if start<end:
        mid=(start+end)//2
        mergesort(a,start,mid)
        mergesort(a,mid+1,end)
        merge(a,start,mid,end)
# divides the list continiously under the logic that the start index is lesser than the end index.
# when the list breaks down to single digits, their start and index is both 0, so the breaking 
# part is over. then, merging is called.
    
mergesort(a,0,len(a)-1)

print(a)