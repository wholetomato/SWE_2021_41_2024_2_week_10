from typing import List
 # Skeleton code for even_list
def even_list(int_list: List[int]) -> List[int]:
    even_int_list = []
    for i in int_list:
        if i % 2 ==0:
            even_int_list.append(i)
    return even_int_list

    """
    Determines if a number is even and return an even list.
    Args:
        int_list: A list of integer.
    Returns:
        A list of even integers.
    """
    # TODO: Implement even_list
    pass
 # Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    sum = 0
    for i in even_int_list:
        sum += i*i
    return sum
    """
    Computes the sum of the squares of all even numbers in a l
    Args:
        even_int_list: A list of even integers.
    Returns:
        The sum of the squares of all even numbers in the lis
 Assignment
 2
    """
    # TODO: Implement sum_of_squares_of_even
    pass
 # Main function
def main():
    # Example list
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)
 # Boilerplate code
if __name__ == "__main__":
    main()