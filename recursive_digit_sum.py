# We define super digit of an integer  using the following rules:

# Given an integer, we need to find the super digit of the integer.

# if n = 5342, k = 4 then 5+3+4+2+5+3+4+2+5+3+4+2+5+3+4+2 = 2

# If x has only 1 digit, then its super digit is x.
# Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k

def superDigit(n, k):
    digits = map(int, list(n))                           
    # map() is used to convert each letter of string to integer and then converted into list
    return get_super_digit(str(sum(digits) * k))         
    # here sum(digits) is used to get the sum of each list element and then multiplied by k to obtain k times

def get_super_digit(p):
    if len(p) == 1:
        # if length of p is 1 return p
        return int(p)
    else:
        digits = map(int, list(p))
        # p is the string from above step and converted to list of integers.
        return get_super_digit(str(sum(digits)))
        # return recursively returning the sum of digits list and converting the result to string
    
n = input("Enter the number: ")
k = int(input("Enter the number of times: "))
result = superDigit(n, k)
print(result)


# https://www.hackerrank.com/challenges/one-week-preparation-kit-recursive-digit-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four