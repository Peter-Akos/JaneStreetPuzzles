from Grid import Grid

if __name__ == '__main__':
    # Example usage:
    file_path = 'small.csv'  # Replace 'example.csv' with your CSV file path
    grid = Grid(file_path)
    print(grid)
    grid.add_black_cells(3)
    grid.update_regions()
    print(grid)
