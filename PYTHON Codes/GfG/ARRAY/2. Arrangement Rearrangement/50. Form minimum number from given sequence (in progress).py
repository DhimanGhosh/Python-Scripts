'''
Given a pattern containing only I's and D's. I for increasing and D for decreasing.
Devise an algorithm to print the minimum number following that pattern.
Digits from 1-9 and digits can't repeat.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is a string, which contains only I's and D's in capital letter.

Output:
Print the minimum number following that pattern.

Example:
Input
5
D
I
DD
IIDDD
DDIDDIID

Output
21
12
321
126543
321654798
'''

def only_I(l):
    return ''.join([str(n) for n in range(len(nums))])

def only_D(l):
    return ''.join([str(n) for n in range(len(nums), 0, -1)])

def run():
    res = ''
    if 'D' not in string:
        res = only_I(n)
    elif 'I' not in string:
        res = only_D(n)
    else:
        for i in range(len(string)):
            if string[i] == 'I':
                for j in range(i+1, len(string)):
                    if string[j] == 'D':
                        break
                res += only_I(j)

            if string[i] == 'D':
                for j in range(i+1, len(string)):
                    if string[j] == 'I':
                        break
                res += only_D(j)
    print(res)


if __name__ == '__main__':
    num_list = [str(n) for n in range(1, 10)]
    string = input('Pattern: ')

    n = len(string)
    nums = num_list[:n+1]
    run()
