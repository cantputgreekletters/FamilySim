from simulation import Simulation
import matplotlib.pyplot as plt
from sys import argv
def ReplicateSimulation(gens : int, n : int = 10000):
    print(f"Replicating for gen {gens}")
    S = 0
    for _ in range(n):
        sim = Simulation(gens)
        S += sim.Simulate()
        
    return S / n

def Main(n = 13) -> None:
    if(n < 3): n = 3
    x = [i for i in range(3,n + 1)]
    y = [ReplicateSimulation(i, 10000) for i in x]
    plt.plot(x,y)
    plt.show()

if __name__ == "__main__":
    try:
        n = int(argv[1])
    except:
        n = 13
    Main(n)