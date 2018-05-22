'''
Shuffle a given array


Following is the detailed algorithm:

To shuffle an array a of n elements (indices 0..n-1):
  for i from n - 1 downto 1 do
       j = random integer with 0 <= j <= i
       exchange a[j] and a[i]

Input: {1, 2, 3, 4, 5, 6, 7, 8}
Output: {7, 8, 4, 6, 3, 1, 2, 5}
'''
import sys
sys.path.insert(0, 'D:\My Own Work\PYTHON Codes\GfG\ARRAY')

from CUSTOM_RANDOM import rand_range

def rand(a):
    n = len(a)

    for i in range(n-1, -1, -1):
        j = rand_range(0,i)
        a[i], a[j] = a[j], a[i]
    return a

def run():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(arr)
    print(rand(arr))

if __name__ == '__main__':
    run()
