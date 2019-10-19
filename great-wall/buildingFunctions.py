
def mirrorCoords(locations):
    rightSide = []
    for locs in locations:
        rightSide.append([27-locs[0], locs[1]])
        #print(output)
    locations+=rightSide
    return locations


def getColumnsLeft(startx):
    x = startx
    y = startx+14
    columnIndices = [[x,y]]
    x+=1
    columnIndices.append([x,y])
    y-=1
    while y>startx:
        columnIndices.append([x,y])
        x+=1
        columnIndices.append([x,y])
        y-=1

    columnIndices.append([x,y])
    return columnIndices


def getColumnsRight(startx):
    x = startx
    y = 27-(x-14)
    columnIndices = [[x,y]]
    x-=1
    columnIndices.append([x,y])
    y-=1
    while y>27-startx:
        columnIndices.append([x,y])
        x-=1
        columnIndices.append([x,y])
        y-=1

    columnIndices.append([x,y])
    return columnIndices
