from random import choice

class RandomWalk():
    """This class generates random walks"""

    def __init__(self, points=5500) -> None:
         """Initialize the Random Walk class"""
         self.points = points

         #Walk initial values (0, 0)
         self.x_values = [0]
         self.y_values = [0]

    def walk(self) -> None:
        """Walk through the points"""

        #Walk ultil all values = points number
        while len(self.x_values) < self.points:
            #Define direction and how far to go in that direction
            direction_x= choice([1, -1])    #Right or left
            distance_x = choice([0, 1, 2, 3, 4])
            step_x = direction_x* distance_x

            direction_y= choice([1, -1])    #Up or down
            distance_y = choice([0, 1, 2, 3, 4])
            step_y = direction_y* distance_y

            #0 it is not a direcion
            if step_x == 0 and step_y == 0:
                continue

            #Calculate the next x and y values getting list last value plus calculated value
            next_x = self.x_values[-1] + step_x
            next_y = self.y_values[-1] + step_y

            #Add new values to the list
            self.x_values.append(next_x)
            self.y_values.append(next_y)
