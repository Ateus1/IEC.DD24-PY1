numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index_of_none = 4
numbers_without_none = numbers[:index_of_none] + numbers[index_of_none+1:]
numbers[index_of_none] = sum(numbers_without_none)/len(numbers)
print("Измененный список:", numbers)
