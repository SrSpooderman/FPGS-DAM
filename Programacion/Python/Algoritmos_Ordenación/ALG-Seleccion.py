array = [7,6,5,5,4,3,1]
for pasada in range (len(array)):
    min = array[len(array)-1]
    min_pos = ""
    for num in range(pasada,len(array)):
        if array[num] < min:
            min = array[num]
            min_pos = num
        elif array[num] > min:
            pass
        elif array[num] == min:
            min = array[num]
            min_pos = num
    aux = array[pasada]
    array[pasada] = min
    array[min_pos] = aux
print(array)