a = 5.08  # 2004 Scotland population(million)
b = 5.33  # 2014 Scotland population(million)
c = 5.55  # 2024 Scotland population(million)
d = b - a  # 2004-2014 population variance
e = c - b  # 2014-202 population variance

# e<d, so the population speed of growth is decrease

X = True
Y = False
W = X or Y 

# X=True, Y=True → W=True
# X=True, Y=False → W=True
# X=False, Y=True → W=True
# X=False, Y=False → W=False