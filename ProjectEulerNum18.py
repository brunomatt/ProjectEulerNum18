#By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#3
#7 4
#2 4 6
#8 5 9 3
#That is, 3 + 7 + 4 + 9 = 23.
#Find the maximum total from top to bottom of the triangle below:
#NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
#However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
#it cannot be solved by brute force, and requires a clever method! ;o)
row1 = [75]
row2 = [95, 64]
row3 = [17, 47, 82]
row4 = [18, 35, 87, 10]
row5 = [20, 4, 82, 47, 65]
row6 = [19, 1, 23, 75, 3, 34]
row7 = [88, 2, 77, 73, 7, 63, 67]
row8 = [99, 65, 4, 28, 6, 16, 70, 92]
row9 = [41, 41, 26, 56, 83, 40, 80, 70, 3]
row10 = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
row11 = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
row12 = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
row13 = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
row14 = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
row15 = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

triangle = [row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12, row13, row14, row15]

for i in range(1,len(triangle)):
    for m in range(0, len(triangle[-2])):
        triangle[-2][m] = triangle[-2][m] + max(triangle[-1][m], triangle[-1][m + 1])
    triangle.pop()

answer = triangle[-1]

print(answer)