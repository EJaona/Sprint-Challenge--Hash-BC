#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in range(len(weights)):
        diff = hash_table_retrieve(ht, limit - weights[i])
        print(diff, limit - weights[i], weights[i])
        if diff is None:
            print(f"diff is not in the table. ")
            hash_table_insert(ht, weights[i], i)
            print(f"diff is now in the table. Value is {weights[i]}, and index of {i} ")
        else:
            print(f"Here is the diff {diff} and i {i}")
            return (i, diff)
    return None



def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
