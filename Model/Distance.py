from math import radians, sin, cos, sqrt, asin
from typing import List, Dict

def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> int:
    R = 6372.8  # Earth radius in kilometers
    distance_coefficient = 1.3
    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return int(distance_coefficient * (R * c))

def DistanceMatrix(locations: List[Dict[str, float]]) -> List[List[int]]:
    distance_matrix = []

    for i in range(len(locations)):
        row = []
        for j in range(len(locations)):
            if i == j:
                row.append(0)
            else:
                lat1, lon1 = locations[i]["lat"], locations[i]["lon"]
                lat2, lon2 = locations[j]["lat"], locations[j]["lon"]
                distance = haversine(lat1, lon1, lat2, lon2)
                row.append(distance)
        distance_matrix.append(row)

    return distance_matrix
