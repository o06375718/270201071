def sum_of_nested_list(x):
    if len(x)==0:
        return 0
    else:
        if isinstance(x,list):
            return sum_of_nested_list(x[0]) + sum_of_nested_list(x[1:])
        else :
            return sum_of_nested_list(x)[0]+sum_of_nested_list(x)[1:]
