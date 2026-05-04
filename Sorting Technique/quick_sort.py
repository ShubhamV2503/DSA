
a = [4,1,2,2,11,13,1]

def sort(a,low,high):

    pivot = a[low]
    i = low
    j = high

    while i < j:
        

def quick_sort(a,low,high):
    if low < high:
        partision = sort(a,low,high)
        quick_sort(a,low,partision)
        quick_sort(a,partision,high)

#TC:
#sc:
