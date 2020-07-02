from test_distance import backtracker, initialize_stuff


arr, arr_old, start, end = initialize_stuff(15, 15)


print(arr)

print(arr_old)


results = []

print(backtracker(arr, 5, 5, results))
