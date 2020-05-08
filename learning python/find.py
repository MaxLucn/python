def find_max(data):
    max = data[0]
    for num in data:
        if max < num:
            max = num
    return max
