from random import choice

def get_step() -> int:
    """Define direction and how far to go in that direction"""
    direction= choice([1, -1])   
    distance= choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
    return direction* distance

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
            #Get X and Y step values
            step_x = get_step()
            step_y = get_step()

            #0 it is not a direcion
            if step_x == 0 and step_y == 0:
                continue

            #Calculate the next x and y values getting list last value plus calculated value
            next_x = self.x_values[-1] + step_x
            next_y = self.y_values[-1] + step_y

            #Add new values to the list
            self.x_values.append(next_x)
            self.y_values.append(next_y)
