'''Duplicate Employee IDs
REMOVE DUPLICATE EMPLOYEE IDs FROM A SORTED PYTHON LIST

Difficulty: 3/10

TASK DESCRIPTION

You've just been hired as a software developer at Puppy Corporation, a start-up company focused on making the world a better place using puppies. Also the company itself is run by puppies.

Unfortunately, there's already some issues at the start-up!

Since the company has been on a hiring spree, they've been logging new employee ids, we can represent these as a Python list, for example:

ids = [1,2,3,4,5]

Here is the issue though, while entering new employee ids, a puppy accidentally sat on the keyboard at times and entered duplicate entries! For example:

ids = [1,1,1,2,2,2,3,3,3,4,4,5]

The company needs you to remove the duplicate employee ids from this array (python list).

Plus, there is one other major issue, the computer used to store the employee ids is a tiny raspberry pi computer with almost no memory (ridiculous I know, but hey, they're just puppies!). This means you will need to do this operation in-place without using another list. Remember this means you aren't allowed to use another data structure, such as a list or set, you need to do this in-place on the original list! (Otherwise the problem is too easy!)

Since you are conducting this operation on the original list (in-place), this means you will have to fill in duplicate

Expected Input:

The list of employee ids will be a Python List as input will always be sorted in increasing order.

Expected Output:

You should return a tuple with two items:  N (the number of unique elements) and the updated list with the unique items.

Example Input and Output:

employee_ids = [1,1,1,2,2,2,3,3,3,4,4,5]
output = (5, [1,2,3,4,5])'''

solve:

def remove_duplicate_ids(ids_list):
    num_enteries = len(ids_list)

    index_to_update = 1

    for i in range(1, num_enteries):

        if ids_list[i] != ids_list[i - 1]:
            ids_list[index_to_update] = ids_list[i]
            index_to_update += 1

    N = index_to_update
    return (N, ids_list[:N])
