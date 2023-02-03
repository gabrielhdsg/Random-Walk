import matplotlib.pyplot as plt
from random_walk import RandomWalk

#Loop to create as many graphs the user desire
graph_num = 1
while True:
    #Create a random walk and plot its points
    walk_obj = RandomWalk()
    walk_obj.walk()

    #Create a new figure
    plt.figure(graph_num)

    point_numbers = list(range(walk_obj.points))
    plt.scatter(walk_obj.x_values, walk_obj.y_values, c=point_numbers, cmap=plt.cm.Reds,
    edgecolor='none', s=10)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='blue', s=60)
    plt.scatter(walk_obj.x_values[-1], walk_obj.y_values[-1], c='green',
    s=60)

    # Comment the axes.
    plt.xlabel("X Coordanate", fontsize=14)
    plt.ylabel("Y Coordanate", fontsize=14)

    plt.savefig('path'+str(graph_num)+'.png', bbox_inches='tight')

    running = input("Do you want a new walk?(y/n)")
    if running ==  'n':
        break
    graph_num+=1

