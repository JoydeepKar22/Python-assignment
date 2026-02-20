from math import inf

def secondLargest(ls: list[int]) -> int :
    """
    Finds the second largest distinct number in a list.

    Args:
        ls (list[int]): A list containing integers.

    Returns:
        int The second largest number in the list. 
                     Returns -inf if no distinct second largest number exists.
    """
    maxi =maxi2= -inf
    
    
    for i in ls:
        if i > maxi:
              maxi2 = maxi
              maxi = i
        elif i > maxi2 and i < maxi:
            maxi2 = i

    return maxi2

ls = [1, 3, 35, 6, 6]
print(secondLargest(ls))