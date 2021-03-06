#this is my python implementation of the von Neumann (merge sort) algorithm
def neumannSort(lt):
    '''
    breaks a list into half its size, sorts the
    splitted version and runs a merge function on them
    '''
    #base case
    if len(lt) < 2:
        return lt
    else:
        #find middle of list
        middle = int(len(lt) / 2)
        #recursive call on left and right half
        left = neumannSort(lt[:middle])
        right = neumannSort(lt[middle:])
        #merge left and right half, by calling merge function
        return merge(left, right, lt)


def merge(left, right, lt):
    '''
    compares members of sorted lists,
    and merges them
    '''
    #initiate iterators
    i, j, k = 0, 0, 0
    #iterate through lists
    while i < len(left) and j < len(right):
        #if first of left is lower, put it in first/next place
        if left[i] <= right[j]:
            lt[k] = left[i]
            #increment iterators by one
            i += 1
            k += 1
        else:
            #if first of right is lower, put it in first/ next place
            lt[k] = right[j]
            #increment iterators by one
            j += 1
            k += 1
    #if right runs out of members, add all remaining members of left to lt
    while (i < len(left)):
           lt[k] = left[i]
           k += 1
           i += 1
    #if left runs out of members, add all remaining members of right to lt
    while (j < len(right)):
           lt[k] = right[j]
           k += 1
           j += 1
    return lt



#usage:
#example list:
l = [10, 5, 6, 2, 9, 7, 8, 1, 4, 3]
#print unsorted list
print l
#run merge sort algorithm
sortedList = neumannSort(l)
#print sorted list
print sortedList





