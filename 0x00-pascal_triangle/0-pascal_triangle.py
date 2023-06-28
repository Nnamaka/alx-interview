#!/usr/bin/python3

def pascal_triangle(n):
    """
    The pascal triangle
    args:
        n - size of pascal triangle
    returns:
        list of lists
    
    """
    sec = n
    main_arr = []

    if (sec <= 0):
        return []
    
    if (sec == 1):
        return [[1]]
    
    if (sec == 2):
        return [[1],[1,1]]
    
    m, n = (0, 1)
    main_arr =  [[1],[1,1]]

    for num in range(2, sec):
        num = num + 1
        work_arr = main_arr[-1]
        small_arr = []

        while( n <= num - 2):
            small_arr.append(work_arr[m] + work_arr[n])
            m = m + 1
            n = n + 1

        small_arr = [1] + small_arr + [1]
        main_arr.append(small_arr)
        m, n = (0, 1)

    return main_arr



