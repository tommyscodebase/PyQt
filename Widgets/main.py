import math

coords = [[1000, 1000]]
b = [125.98, 56, 12, 17]
c = [63.25, 73, 45, 3]
d = [117.81, 16, 12, 49]

deps, lats = [], []

for item in b, c, d:
    dep = item[0] * math.sin(item[1] + item[2] / 60 + item[3] / 3600)
    lat = item[0] * math.cos(item[1] + item[2] / 60 + item[3] / 3600)
    deps.append(dep)
    lats.append(lat)

lines = ["A - B", "B - C", "C - D"]

for x, y in zip(deps, lats):
    easting = coords[-1][0] + x
    northing = coords[-1][1] + y
    coords.append([easting, northing])
    print(f"Coordinates of {lines[deps.index(x)]}: {easting, northing}")
