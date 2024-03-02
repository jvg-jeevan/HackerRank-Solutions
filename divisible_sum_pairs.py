# Given an array of integers and a positive integer , determine the number of (i, j) pairs where i< j and ar[i] + ar[j] is divisible by k.

def divisibleSumPairs(n, k, ar):
    # Write your code here
    countof = 0
    for i in range(n):
        # this is to avoid choosing the same element can also be done as for j in range(i+1, n): 
        for j in range(i+1, n):            
            if (ar[i] + ar[j]) % k == 0:
                countof+=1
                
    return countof

print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))


# https://www.hackerrank.com/challenges/three-month-preparation-kit-divisible-sum-pairs/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one 