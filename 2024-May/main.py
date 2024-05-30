from src.grid import Grid

if __name__ == '__main__':
    file_path = 'src/small.csv'
    grid = Grid(file_path)
    print(grid)
    print(grid.region_lookup)
    print(grid.table)
    print(grid.table_size)
    grid.solve()
