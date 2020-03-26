import numpy as np
a0 = 3.52 / np.sqrt(2)
c0 = np.sqrt(8 / 3.0) * a0
from ase.io import Trajectory
traj = Trajectory('trajectories/Ni.traj','w')
from ase.build import bulk
from ase.calculators.emt import EMT
eps = 0.01
for a in a0 * np.linspace(1 - eps, 1 + eps, 3):
    for c in c0 * np.linspace(1 - eps, 1 + eps, 3):
        ni = bulk('Ni', 'hcp', a=a, c=c)
        ni.set_calculator(EMT())
        ni.get_potential_energy()
        traj.write(ni)