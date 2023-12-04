'''Permutations of Security Codes
PERMUTATIONS OF SECURITY CODES

Difficulty: 4/10

TASK DESCRIPTION

Puppy Corporation has decided to implement a laptop security code system. They will attach a keypad to each laptop that has some numbers on it. If a puppy enters the correct security code into the keypad, the laptop will unlock. There is one issue though, each number can only be used once! To help with this issue, the puppies could add more available numbers to the numpad, but how many unique numbers is enough?

The puppies have decided that due to this limitation of each number only being able to be used once, they will need your help to create a program to calculate every possible permutation given a list of numbers available on the numpad, if every number has to be used at least once.

Expected Input:

The list of numbers available on the keypad will be a Python List as input.

Expected Output:

You should return a list with all possible permutations that uses all numbers on the numpad. Remember that permutations are not the same as combinations, permutations that share the same numbers but in different order count as different permutations. For example, the passcode [1,2,3] is not the same as the passcode [3,2,1], thus both permutations should be included in your output.

Example Input and Output:

numpad_list = [1,2,3]
permutations = ([1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1])

numpad_list = [1,2]
permutations = ([1,2],[2,1])


Note: the solution file is set-up for you to solve this recursively.'''


#solve:

def create_permutations(numpad_list):
    """
    INPUT:
        numpad_list: The list of unique values on the numpad
    OUPUT:
        permutations_output: The list of lists containing all permutations.
    """

    def permutation_looper(first_number_index=0):
        '''
        While you don't technically need to use recursion,
        our solution uses a nested function here.
        '''
        '''
        This is our resursive function. We simply provide it the index value of
        the original location of first number in the current permutation.

        For example, if our numpad_list is [1,2,3] than first_number_index=0 is
        the integer 1 (which corresponds to permutations [1,2,3] and [1,3,2]

        Once first_number_index == n (for example if numpad_list is [1,2,3] than once
        first_number_index==2 then we have permutations starting at the last number,
        meaning we've created all possible permutations.
        '''
        # If the index of the first_number in the permutation
        # is equal to our current n length of numpad_list, we are done
        # creating permutations!
        if first_number_index == n:
            permutations_output.append(numpad_list[:])

        for i in range(first_number_index, n):
            # Go through numpad_list, starting at our current
            # "first_number_index".
            numpad_list[first_number_index], numpad_list[i] = numpad_list[i], numpad_list[first_number_index]

            # Continue resursively to use the next numbers
            # to create the permutations
            permutation_looper(first_number_index + 1)

            # Now reset the values again, since we have called
            # permutation_looper again.
            numpad_list[first_number_index], numpad_list[i] = numpad_list[i], numpad_list[first_number_index]

    # N is the current length of the numpad_list
    n = len(numpad_list)
    # This is the output you provide
    permutations_output = []
    # This is our first call of the nested recursive function.
    permutation_looper()
    # Once the recursion finishes, we return the final list.
    return permutations_output
