import csv
from typing import List

from src.helper_functions import power_of_7, fibonacci, multiple_of_5, cube, palindrome


class Grid:
    def __init__(self, file_path):
        self.file_path = file_path
        self.regions = None
        self.region_lookup = {}
        self.table = None
        self.black_box_history = {}
        self.table_size = 0
        self.read_csv()
        self.init_regions()
        self.function_lookup = {}
        self.initialize_function_lookup()

    def __str__(self):
        # Determine the maximum width needed for each cell
        max_width = max(len(str(cell)) for row in self.regions for cell in row)

        # Create a string representation of the grid with even spacing
        return "\n" + '\n'.join([' '.join(str(cell).ljust(max_width) for cell in row) for row in self.table])

    def read_csv(self):
        self.regions = []
        self.table = []
        with open(self.file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                self.regions.append(row)
                self.table.append([-1 for _ in row])
                self.table_size += 1

    def init_regions(self):
        # Create a dictionary with the region names as keys and the positions as values
        for i, row in enumerate(self.regions):
            for j, cell in enumerate(row):
                if cell in self.region_lookup:
                    self.region_lookup[cell].append((i, j))
                else:
                    self.region_lookup[cell] = [(i, j)]

    def solve(self, current_x=0, current_y=0):
        if self.valid_solution():
            print(self)
            return
        for possible_choice in range(-1, 10):
            if possible_choice == -1:
                self.insert_black_box(current_x, current_y)

    def valid_solution(self) -> bool:
        numbers = self.get_numbers()
        for number, row in numbers:
            if self.function_lookup[row](number) is False:
                return False
        return True

    def insert_black_box(self, x, y):
        region_id = self.regions[x][y]

    def get_numbers(self) -> List[List[int]]:
        result = []
        for row_number, row in enumerate(self.table):
            current_number = 0
            current_number_initialized = False  # we need this so we can recognize 0 as a number
            for cell in row:
                if cell == -1 and current_number_initialized:
                    result.append([current_number, row_number + 1])
                    current_number_initialized = False
                    current_number = 0
                elif cell != -1:
                    current_number = current_number * 10 + cell
                    current_number_initialized = True
            if current_number_initialized:
                result.append([current_number, row_number + 1])
        return result

    def initialize_function_lookup(self):
        if self.table_size == 5:
            self.function_lookup = {
                1: power_of_7,
                2: fibonacci,
                3: multiple_of_5,
                4: cube,
                5: palindrome,
            }
