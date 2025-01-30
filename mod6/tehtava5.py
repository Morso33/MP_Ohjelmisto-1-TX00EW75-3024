def return_evens(list):
    tmp_list = []
    for i in list:
        if i % 2 == 0:
            tmp_list.append(i)
    return tmp_list

test_list = [1, 2, 3, 4, 5]
print(return_evens(test_list))