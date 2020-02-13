def binary_search(target, my_list):
    my_dict = dict(enumerate(my_list))
    end_index = len(my_dict)-1
    mid_index = end_index//2
    mid_int = my_dict[mid_index]

    if target < my_list[0] or target > my_list[end_index]:
        return('does not exist')

    while True:
        half = (end_index-mid_index)//2
        if half < 1:
            half = 1

        if target == mid_int:
            return(mid_index)
        elif(target < mid_int):
            end_index = mid_index-1
            mid_index = mid_index-half
            mid_int = my_dict[mid_index]
        else:
            mid_index = mid_index+half
            mid_int = my_dict[mid_index]


print(binary_search(56, list(range(1, 201))))
