def get_percentage(number, precision=None):
    return str(round(number * 100, precision)) + "%"
#
#
# number = float(input())
# precision = int(input())
#
# print(get_percentage(number))
# print(get_percentage(number, precision))
#
# print(round(0.0123 * 100, 0))