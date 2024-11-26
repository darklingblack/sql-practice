def near(lat1, long1, lat2, long2):
    if (abs(lat1 - lat2) < 1) and (abs(long1 - long2) < 1):
        near = True
    else:
        near = False
    return near


1. Point 1: latitude = 29.65, longitude = -82.33. Point 2: latitude = 41.74, longitude = -111.83.
2. Point 1: latitude = 29.65, longitude = -82.33. Point 2: latitude = 30.5, longitude = -82.8.
3. Point 1: latitude = 48.86, longitude = 2.35. Point 2: latitude = 41.89, longitude = 2.5.

#1
lat1 = 29.65; long1 = -82.33; lat2 = 41.74; long2 = -111.83

near(29.65, -82.33, 41.74, -111.83)

#2
lat1 = 29.65; long1 = -82.33; lat2 = 30.5; long2 = -82.8
near(lat1, long1, lat2, long2)

#3
lat1 = 48.86; long1 = 2.35; lat2 = 41.89; long2 = 2.5
near(lat1, long1, lat2, long2)
