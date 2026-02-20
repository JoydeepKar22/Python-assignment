import logging

logging.basicConfig(
    filename="remove_duplicates.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def remove_duplicates(input_list: list[int]) -> list[int]:
    """
    Removes duplicate elements from a list while preserving the original order.
    Parameters:
        input_list (list[int]): The list containing potential duplicates
    Returns:
        list[int]: A new list with duplicates removed
    """
    logging.info(f"Removing duplicates from list: {input_list}")
    
    seen = set()
    result = []
    
    for item in input_list:
        if item not in seen:
            result.append(item)
            seen.add(item) 
            
    logging.info(f"List after removing duplicates: {result}")
    return result


numbers = [1, 2, 2, 3, 1, 4, 2]
result = remove_duplicates(numbers)

print("List without duplicates:")
print(result)