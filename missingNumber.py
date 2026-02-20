import logging

logging.basicConfig(
    filename="missing_number.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def missing_number(nums: list[int], n: int) -> int:
    """
    Finds the missing number in a given sequence from 1 to n.
    Parameters:
        nums (list[int]): List of numbers with one missing
        n (int): The maximum number in the complete sequence
    Returns:
        int: The missing number
    """
    logging.info(f"Finding missing number in sequence up to {n}: {nums}")
   
    expected_sum = n * (n + 1) // 2  
    actual_sum = sum(nums)
    missing_val = expected_sum - actual_sum
    
    logging.info(f"Missing number successfully calculated: {missing_val}")
    return missing_val

my_list = [1, 2, 4, 5]
n = 5
result = missing_number(my_list, n)

print("The missing number is:")
print(result)