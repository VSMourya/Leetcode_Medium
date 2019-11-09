

def getMinDistance(houses,stores):


    return [ min([store_pos for store_pos in stores], key=lambda x: abs(x - house_pos))  for house_pos in houses ]

    # or


    # ls = []
    # for house_pos in houses:
    #     minimum = min([store_pos for store_pos in stores], key=lambda x: abs(x - house_pos))
    #     ls.append(minimum)
    #
    # return ls



houses = [4, 8, 1, 1]
stores = [5, 3, 1, 2, 6]

print(getMinDistance(houses,stores))



