import math

filepath = r"C:\Users\loann\Downloads\video2_values_0_200.txt"
with open(filepath, 'r') as f:
    data = []
    for line in f:
        values = line.strip().split()
        line_data = [values[i:i+3] for i in range(0, len(values), 3)]
        data.append(line_data)

    distances = []
    for line in data:
        point1back = (float(line[6][0]), float(line[6][1]))
        point2back = (float(line[7][0]), float(line[7][1]))
        distanceback = math.sqrt((point2back[0] - point1back[0])**2 + (point2back[1] - point1back[1])**2)
        point1paw = (float(line[15][0]), float(line[15][1]))
        point2paw = (float(line[17][0]), float(line[17][1]))
        distancepaw = math.sqrt((point2paw[0] - point1paw[0])**2 + (point2paw[1] - point1paw[1])**2)
        print("The size of the paw is : ",distancepaw)
        distances.append(distanceback/distancepaw)
    max_distance = max(distances)
    for i, distance in enumerate(distances):
        distances[i] = distance/max_distance
        angle = math.asin(distances[i])
        #Conversion factor
        rad_to_deg = 180/math.pi

        #Converting to degree
        angle = angle* rad_to_deg
        print("The angle of the dog for the frame ", i," is : ", angle)
