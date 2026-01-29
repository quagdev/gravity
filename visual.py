import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import CheckButtons

from main import Body, get_net_force 

figure, ax = plt.subplots()
plt.subplots_adjust(left = 0.2)

sun = Body("Sun", 1.989e30, [0, 0], [0, 0], "yellow")
earth = Body("Earth", 5.972e24, [1.496e11, 0], [0, 29780], "blue")
bodies = [sun, earth]