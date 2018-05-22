'''
Reorder an array according to given indexes

Example:
Input:  arr[]   = [10, 11, 12];
        index[] = [1, 0, 2];
Output: arr[]   = [11, 10, 12]
        index[] = [0,  1,  2] 

Input:  arr[]   = [50, 40, 70, 60, 90]
        index[] = [3,  0,  4,  1,  2]
Output: arr[]   = [40, 60, 90, 50, 70]
        index[] = [0,  1,  2,  3,   4] 
'''
def reorder3(a, i): # [2nd array] <O(n)> [< TIME, > Space]
    a1 = [0]*len(a)
    for j in range(len(a)):
        a1[i[j]] = a[j]
    for j in range(len(a)):
        i[j] = j
        a[j] = a1[j]
    return [a, i]

def reorder2(a, i): # [Same array] <O(n2)> [> TIME, < Space]
    for j in range(len(a)-1):
        for k in range(j+1, len(i)):
            if i[k] == j:
                i[k], i[j] = i[j], i[k]
                a[k], a[j] = a[j], a[k]
                break
    return [a, i]

def reorder1(a, i): # Use Dictionary, Bind two arrays as indexes as keys [2nd array] <O(n)> [< TIME, > Space]
    a1 = {}
    for j in range(len(a)): #Dictionary Binding
        a1[i[j]] = a[j]
    a2 = []
    for j in range(len(a)):
        a2.append(a1[j])
    return a2

def reorder(a, i): # [2nd array] <O(n2)> [> TIME, > Space]
    a1 = []
    for j in range(len(a)):
        for k in range(len(i)):
            if i[k] == j:
                a1.append(a[k])
    return a1

def run():
    arr = [50, 40, 70, 60, 90]
    index = [3,  0,  4,  1,  2]

    print(str(arr) + '\n' + str(index))
    result = reorder2(arr, index)
    print(str(result[0]) + '\n' + str(result[1]))

if __name__ == '__main__':
    run()
