# In class work
# Date: 11/2/21

def transform_triangle(x, y, how='clockwise'):
    x_t = 0
    y_t = 0
    if how == 'clockwise':
        x_t = y
        y_t = -x
    elif how == 'counter clockwise':
        x_t = -y
        y_t = x
    else:
        print('invalid direction')
    return x_t, y_t


point_1 = [5, 5]
point_2 = [6, 2]
point_3 = [3, 2]

print('| Original Triangle |')
print(point_1)
print(point_2)
print(point_3)
print()

new_point_1 = transform_triangle(point_1[0], point_1[1], how='clockwise')
new_point_2 = transform_triangle(point_2[0], point_2[1], how='clockwise')
new_point_3 = transform_triangle(point_3[0], point_3[1], how='clockwise')

print('| Transformed Triangle Clockwise |')
print(new_point_1)
print(new_point_2)
print(new_point_3)
print()

new_point_1 = transform_triangle(point_1[0], point_1[1], how='counter clockwise')
new_point_2 = transform_triangle(point_2[0], point_2[1], how='counter clockwise')
new_point_3 = transform_triangle(point_3[0], point_3[1], how='counter clockwise')

print('| Transformed Triangle Counter Clockwise |')
print(new_point_1)
print(new_point_2)
print(new_point_3)
print()





