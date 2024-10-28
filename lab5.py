import data
from data import Time
from data import Point


# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(time1: Time, time2: Time):
        total_seconds = time1.second + time2.second #adds total seconds
        total_minutes = time1.minute + time2.minute + (total_seconds // 60) #adds total minutes
        total_hours = time1.hour + time2.hour + (total_minutes // 60) #adds total hours
        return Time(total_hours, total_minutes % 60, total_seconds % 60)

# Part 4
def is_descending(lst: list[float]) -> bool:
    if len(lst) < 2:  # check if the list has 2 elements
        return True  # returns tru if there is one or less elements
    else:
        for i in range(1, len(lst)):  # looks at the entire list
            if lst[i] >= lst[i - 1]:  # compares the current index to that of the previous index
                return False  # returns false if the index being looked at is bigger than that of the previous
            else:
                return True  # returns true the list is in descending order

# Part 5
def largest_between(lst:list[int], lower:int, upper:int):
    if lower > upper or lower < 0 or upper >= len(lst):
        return None #makes sure that the lower bound is greater than the upper
    max_index = lower
    for i in range(lower + 1, upper + 1): #goes through all numbers in the range
        if lst[i] > lst[max_index]:
            max_index = i #compares the two indexes next to each other to see which one is larger
    return max_index

# Part 6
def furthest_from_origin(lst:list[Point]) -> int:
    max_index = 0 #Makes the first point the furthest
    max_distance_squared = lst[0].x ** 2 + lst[0].y ** 2 #Squared distance of first point
    for i in range(1, len(lst)):
        distance_squared = lst[i].x**2 + lst[i].y**2 #Square distance of current index
        if distance_squared > max_distance_squared: #Compares the current index with the max one than replaces it if distance is longer
            max_distance_squared = distance_squared
            max_index = i
    return max_index #Return the index of the furthest point