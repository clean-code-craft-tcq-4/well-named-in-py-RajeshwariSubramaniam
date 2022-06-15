from get_color_codes import (
    get_color_from_pair_number,
    get_pair_number_from_color
)


def get_colors(pair_number):
    major, minor = get_color_from_pair_number(pair_number)
    print(f'Color coding for {pair_number} '
          f'is {major} and {minor}')


def get_pair_number(major_color, minor_color):
    pair_number = get_pair_number_from_color(major_color, minor_color)
    print(f'Pair number for {major_color} and {minor_color} '
          f'is {pair_number}')


if __name__ == '__main__':
    get_colors(24)
    get_pair_number(
        major_color='White',
        minor_color='Brown'
    )
