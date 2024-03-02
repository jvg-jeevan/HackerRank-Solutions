# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def diagonalDifference(arr):
    # Write your code here
    sum1 = sum2 = 0                 
    for i in range(n):
        sum1 += arr[i][i]            
        # accessing diagonal elements such as arr[0][0], arr[1][1], arr[2][2] and adding them
        sum2 += arr[i][n-i-1]        
        # accessing diagonal elements such as a[0][2], arr[1][1], arr[2][0] and adding them
    return abs(sum1 - sum2)          
    # abs() gives the absolute difference i.e |sum1 - sum2|

a = [[11, 2, 4, 9],
     [4, 5, 6, 2],
     [10, 8, -12, 7],
     [2, 7, 4, 9]]
n = len(a)
print(diagonalDifference(a))

# https://hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two