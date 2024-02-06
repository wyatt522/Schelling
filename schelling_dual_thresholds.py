import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm, LinearSegmentedColormap
from collections import deque

class schelling_dual_thresholds:
    def __init__(self, population_frac, satisfy_threshold1, satisfy_threshold2 = 0, threshold_proportion = 1):
        # Define the relative positions of the 8 neighbors
        self.neighbor_offsets_8 = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1),           (0, 1),
                    (1, -1), (1, 0), (1, 1)]

        self.population_frac = population_frac
        self.satisfy_threshold1 = satisfy_threshold1
        self.satisfy_threshold2 = satisfy_threshold2
        self.threshold_proportion = threshold_proportion

        array_2d = np.empty((50, 50), dtype=tuple)
        for i in range(50):
            for j in range(50):
                array_2d[i, j] = (0, 0)

        self.map = array_2d


        self.randomize_map(self.population_frac, self.satisfy_threshold1, self.satisfy_threshold2, self.threshold_proportion)


    def randomize_map(self, population_frac, threshold_1, threshold_2=0, t_proportion=1):
        # Set the total number of elements to be updated
        total_updates = int(population_frac*1250)


        all_indices = np.arange(2500)
        

        # Randomly choose indices for 1s and 2s
        indices_1 = np.random.choice(all_indices, total_updates, replace=False)
        remaining_indices = np.setdiff1d(all_indices, indices_1)
        indices_2 = np.random.choice(remaining_indices, total_updates, replace=False)
  

        secondary_thresholds = int(t_proportion*2500)

        # Set values at chosen indices
        for indice in indices_1:
            self.map.flat[indice] = (1, threshold_2)

        for indice in indices_1[0:secondary_thresholds]:
             self.map.flat[indice] = (1, threshold_1)
        
        for indice in indices_2:
            self.map.flat[indice] = (2, threshold_2)

        for indice in indices_2[0:secondary_thresholds]:
             self.map.flat[indice] = (2, threshold_1)

    @staticmethod
    def inbounds(point):
        return 50 > point[0] >= 0 and 50 > point[1] >= 0

    def count_neighbors(self, type, point):
        count = 0
        for offset in self.neighbor_offsets_8:
            temp_point = (point[0] + offset[0], point[1] + offset[1])
            if schelling_dual_thresholds.inbounds(temp_point) and self.map[temp_point][0] == type:
                count += 1
        return count
    
    
    def plot_map(self, iteration):
        cmap_colors = [(1, 1, 1), (1, 0, 0), (0, 0, 1)]  # White, Red, Blue
        cmap = LinearSegmentedColormap.from_list('custom', cmap_colors, N=3)
        bounds=[0, 1, 2, 3]
        norm = BoundaryNorm(bounds, cmap.N)

        # extract type data from map
        data_to_plot = np.array([[value[0] for value in row] for row in self.map])

        # tell imshow about color map so that only set colors are used
        plt.imshow(data_to_plot,interpolation='nearest', cmap = cmap,norm=norm)
        plt.axis('off')
        plt.title("P = " + str(self.population_frac) + ", T = " + str(self.satisfy_threshold1) + ", Iteration = " + str(iteration))

        # save plot
        plt.savefig("iteration" + str(iteration) + "p" + str(int(self.population_frac*100)) + "t" + str(self.satisfy_threshold1) + ".png")
        
        # Display the plot
        plt.show()

    def find_closest_satisfied(self, t_satisfy, cell):
        queue = deque()
        visited = set()

        queue.append(cell)
        visited.add(cell)

        while queue:
            current_cell = queue.popleft()

            if self.count_neighbors(self.map[cell][0], current_cell) >= t_satisfy and self.map[current_cell][0] == 0:
                return current_cell

            for offset in self.neighbor_offsets_8:
                temp_point = (current_cell[0] + offset[0], current_cell[1] + offset[1])
                if temp_point not in visited and schelling_dual_thresholds.inbounds(temp_point):
                    queue.append(temp_point)
                    visited.add(temp_point)

        # nothing found return negatives to signal error
        return (-1, -1)
    
    def run_sim(self, steps):
        for i in range(steps):
            iteration = i // 2500
            if i % (steps//4) == 0:
                self.plot_map(iteration)
            i = i % 2500           
            x = i//50
            y = i % 50
            closest_match = self.find_closest_satisfied(self.map[(x, y)][1], (x, y))
            if closest_match != (x, y) and closest_match != (-1, -1):
                self.map[closest_match] = self.map[x, y]
                self.map[x, y] = (0, 0)
        self.plot_map(steps//2500)
            
            