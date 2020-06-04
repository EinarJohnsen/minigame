def create_map(input_str):

    with open(input_str) as f:
        data = f.readlines()

    data = [x.split("\n")[0] for x in data]

    my_dict = {}

    counter = 0
    for element in data:
        for i,x in enumerate(element):
            my_dict[(counter, i)] = x
        counter += 1 

    return my_dict