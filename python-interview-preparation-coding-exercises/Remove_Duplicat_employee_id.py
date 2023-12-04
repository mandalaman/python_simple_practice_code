def remove_duplicate_ids(ids_list):
    num_enteries = len(ids_list)

    index_to_update = 1

    for i in range(1, num_enteries):

        if ids_list[i] != ids_list[i - 1]:
            ids_list[index_to_update] = ids_list[i]
            index_to_update += 1

    N = index_to_update
    return (N, ids_list[:N])