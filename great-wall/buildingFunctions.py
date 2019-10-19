
def mirrorCoords(locations):
    rightSide = []
    for locs in locations:
        rightSide.append([27-locs[0], locs[1]])
        #print(output)
    locations+=rightSide
    return locations
