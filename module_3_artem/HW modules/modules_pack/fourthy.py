import matplotlib.pyplot as plt
from first import my_fn
from second import ran

def graf():
    xPoints = []
    for point in range(20):
        xPoints.append(my_fn(ran()))
    return xPoints

plt.plot(graf(), linestyle='dotted', marker='o')
plt.show()

