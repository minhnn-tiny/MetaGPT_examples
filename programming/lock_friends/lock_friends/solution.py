## solution.py
from typing import List

class Solution:
    def __init__(self, friends: List[int], houses: List[int], times: List[List[int]]):
        self.friends = friends
        self.houses = houses
        self.times = times

    def solve(self) -> List[int]:
        """
        Finds the sequence block of friends and houses that minimizes the total time spent visiting houses.

        :return: A list of the friends in the order they should visit the houses.
        """

        # Sort the friends in ascending order of the time they will visit the first house.
        friends_sorted = sorted(self.friends, key=lambda friend: self.times[friend][0])

        # Initialize the earliest time for each house.
        earliest_times = [0] * len(self.houses)

        # Iterate over the friends in sorted order.
        for friend in friends_sorted:
            # Find the house that has the earliest time that the friend has not yet visited.
            house = -1
            min_time = float('inf')
            for i in range(len(self.houses)):
                if self.times[friend][i] >= earliest_times[i] and self.times[friend][i] < min_time:
                    house = i
                    min_time = self.times[friend][i]

            # If there is no house that the friend has not yet visited, then output -1 to indicate that there is no valid sequence block.
            if house == -1:
                return [-1]

            # Assign the friend to the house and update the earliest time for that house.
            earliest_times[house] = self.times[friend][house]

        # Return the list of friends in the order they should visit the houses.
        return friends_sorted
