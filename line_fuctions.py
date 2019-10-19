def get_line_points(start, end):
    line_points = []

    # Flip so we always go the right
    if start[0] > end[0]:
        temp = start
        start = end
        end = temp

    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    slope = (y2-y1)/(x2-x1)
    x = x1
    y = y1

    print('X = ' + str(x))
    while(x <= x2):

        new_point = [x, round(y)]
        print(new_point)
        if new_point not in line_points:
            line_points.append(new_point)

        x += 1
        y += slope
    return line_points


print(get_line_points([1, 2], [5, 5]))
