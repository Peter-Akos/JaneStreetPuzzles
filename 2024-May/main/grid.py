import csv
import random


class Grid:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []
        self.regions = {}
        self.read_csv()
        # print(self.data)
        self.init_regions()
        # print(self.regions)

    def __str__(self):
        # Determine the maximum width needed for each cell
        max_width = max(len(str(cell)) for row in self.data for cell in row)

        # Create a string representation of the grid with even spacing
        return "\n"+'\n'.join([' '.join(str(cell).ljust(max_width) for cell in row) for row in self.data])

    def read_csv(self):
        with open(self.file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                self.data.append(row)

    def init_regions(self):
        # Create a dictionary with the region names as keys and the positions as values
        for i, row in enumerate(self.data):
            for j, cell in enumerate(row):
                if cell in self.regions:
                    self.regions[cell].append((i, j))
                else:
                    self.regions[cell] = [(i, j)]

    def update_regions(self):
        # Create a 2D list to keep track of visited cells
        visited = [[False] * len(self.data[0]) for _ in range(len(self.data))]

        # Clear the current regions
        self.regions = {}

        # Iterate over all cells
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                # If the cell is not black and has not been visited yet
                if self.data[i][j] != -1 and not visited[i][j]:
                    # Start a new region from this cell
                    region = []
                    region_name = self.data[i][j]
                    self.dfs(i, j, visited, region, region_name)

                    # If the region is not empty, add it to the list of regions
                    if region:
                        region_name = self.data[i][j]
                        if region_name in self.regions:
                            region_name = str(len(self.regions) + 1)
                        self.regions[region_name] = region
                        for m, n in region:
                            self.data[m][n] = region_name


