import logging

logging.basicConfig(
    filename="count_vowels.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def count_vowels(s: str) -> int:
    """
    Count the number of lowercase vowels in a given string.
    Parameters:
        s(str): The input string to check for vowels
    Returns:
        int: The total count of vowels found
    """
    logging.info(f"Counting vowels in the string: '{s}'")
    
    count = 0
    for i in s:
        if i in "aeiou":
            count += 1
            
    logging.info(f"Total vowels counted: {count}")
    return count


s = input("enter the string: ")
result = count_vowels(s)

print("Total vowel count:")
print(result)