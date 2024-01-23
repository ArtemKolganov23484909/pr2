from lvls.classes import Square



def read_numbers_from_file(filename, window):
    numbers = []
    with open(filename, 'r') as file:
        for line_num, line in enumerate(file):
            row_numbers = [int(num) for num in line.strip().split(', ')]
            numbers.extend(row_numbers)
            for col_num, num in enumerate(row_numbers):
                if num != 0:
                    x = 57 + 55 * col_num
                    y = 57 + 55 * line_num
                    square = Square(x, y, k=num)
                    square.draw(window)
    
    return numbers


def get_speed(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)