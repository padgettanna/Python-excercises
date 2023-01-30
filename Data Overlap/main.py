file_1 = open("file1.txt", "r").readlines()
file_2 = open("file2.txt", "r").readlines()
result = [int(num) for num in file_1 if num in file_2]
print(result)
