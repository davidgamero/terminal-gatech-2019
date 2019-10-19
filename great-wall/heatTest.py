d = [[-1, -1, 2, 2, -1, -1], [-1, -1, 0, -1, -1, 0]]
heatMap = map(lambda row:
              " ".join(map(lambda item: '_' if item == -1 else str(item), row)), d)
for row in heatMap:
    print(row)
