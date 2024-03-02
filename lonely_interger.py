# Given an array of integers, where all elements but one occur twice, find the unique element.

def lonelyinteger(a):            
    # creating two lists to add unique elements and also duplicate elements
    # unique list contain the value occur only once unlike duplicate list

    uni = [] 
    dup= []            
    for i in a:
        if i not in uni:
            uni.append(i)
        elif i not in dup:
            dup.append(i)

    #finding the value i.e not in dupliicate list gives the unique element
    for i in uni:                    
        if i not in dup:
            return i
        
arr = [1, 2, 3, 2, 4, 1 ,3]       
print(lonelyinteger(arr))

# https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two