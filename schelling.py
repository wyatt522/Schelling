import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm, LinearSegmentedColormap

class Schelling:

    

    def __init__(self, population_frac, satisfy_threshold) -> None:
        # Define the relative positions of the 8 neighbors
        self.neighbor_offsets_8 = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1),           (0, 1),
                    (1, -1), (1, 0), (1, 1)]

        self.population_frac = population_frac
        self.satisfy_threshold = satisfy_threshold

        self.map = np.zeros((50, 50))


        self.randomize_map(self.population_frac)
        

    def randomize_map(self, population_frac):
        # Set the total number of elements to be updated
        total_updates = int(population_frac*1250)

        all_indices = np.arange(2500)

        # Randomly choose indices for 1s and 2s
        indices_1 = np.random.choice(all_indices, total_updates, replace=False)
        remaining_indices = np.setdiff1d(all_indices, indices_1)
        indices_2 = np.random.choice(remaining_indices, total_updates, replace=False)

        # Set values at chosen indices
        self.map.flat[indices_1] = 1
        self.map.flat[indices_2] = 2

    @staticmethod
    def inbounds(point):
        return 50 > point[0] >= 0 and 50 > point[1] >= 0

    def count_neighbors(self, type, point) -> int:
        count = 0
        for offset in self.neighbor_offsets_8:
            temp_point = (point[0] + offset[0], point[1] + offset[1])
            if Schelling.inbounds(temp_point) and self.map[temp_point] == type:
                count += 1
        return count
    
    
    def plot_map(self):
        cmap_colors = [(1, 1, 1), (1, 0, 0), (0, 0, 1)]  # White, Red, Blue
        cmap = LinearSegmentedColormap.from_list('custom', cmap_colors, N=3)
        bounds=[0, 1, 2, 3]
        norm = BoundaryNorm(bounds, cmap.N)

        # tell imshow about color map so that only set colors are used
        plt.imshow(self.map,interpolation='nearest', cmap = cmap,norm=norm)
        plt.axis('off')
        
        # Display the plot
        plt.show()
    