numbers = [[1,2,3,4],[5,6,7,8]]
numbers2 = [[9,10,11,12],[13,14,15,16]]

# multiply each element with each corresponding number of the other list

for i in range(len(numbers)):
    for j in range(len(numbers[0])):
        print(numbers[i][j] * numbers2[i][j],end = '   ')
    print()