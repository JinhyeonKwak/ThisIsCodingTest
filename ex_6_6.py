# 계수 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    num = array[i]
    count[num] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')


# 반복 연습 1

# count = [0] * (max(array) + 1)
#
# for x in array:
#     count[x] += 1
#
# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i, end=' ')

