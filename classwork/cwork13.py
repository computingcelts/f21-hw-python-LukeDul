# In class work
# Date: 11/2/21

def rotate_90(x, y):
    return y, -x


point_1 = [5, 5]
point_2 = [6, 2]
point_3 = [3, 2]

new_point_1 = rotate_90(point_1[0], point_1[1])
new_point_2 = rotate_90(point_2[0], point_2[1])
new_point_3 = rotate_90(point_3[0], point_3[1])

print('|Original Triangle|')
print(point_1)
print(point_2)
print(point_3)
print()
print('|Transformed Triangle|')
print(new_point_1)
print(new_point_2)
print(new_point_3)

