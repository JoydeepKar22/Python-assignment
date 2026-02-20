import logging
from math import inf

logging.basicConfig(
    filename="second_largest.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def secondLargest(ls: list[int]) -> int | float:
    """
    Finds the second largest distinct number in a list.
    Parameters:
        ls : A list containing integers
    Returns:
        int | float: The second largest number in the list. Returns -inf if no second largest number exists.
    """
    logging.info(f"Finding the second largest number in the list: {ls}")
    
    maxi = maxi2 = -inf
    
    for i in ls:
        if i > maxi:
            maxi2 = maxi
            maxi = i
        elif i > maxi2 and i < maxi:
            maxi2 = i

    logging.info(f"Second largest number found: {maxi2}")
    return maxi2


ls = [1, 3, 35, 6, 6]
result = secondLargest(ls)

print("Second largest number:")
print(result)