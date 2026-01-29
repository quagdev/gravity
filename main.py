import numpy as np

class Body: 
    def __init__ (self, name, mass, pos, vel, color):
        self.name = name
        self.mass = mass
        self.pos = np.array(pos, dtype = float)
        self.vel = np.array(vel, dtype = float)
        self.color = color
        self.trail = []
    def apply_force(self, force_vector, dt):
        acc = force_vector / self.mass
        self.vel += acc * dt
        self.pos += self.vel * dt

def get_net_force(target, all):
    G = 6.674e-11
    net_force = np.array([0.0, 0.0])

    for other in all:
        if target is other: continue

        r_vec = other.pos - target.pos
        dist = np.linalg.norm(r_vec)

        force_mag = G* target.mass * other / (dist**2)
        unit_vec = r_vec / dist

        net_force += force_mag * unit_vec
    
    return net_force