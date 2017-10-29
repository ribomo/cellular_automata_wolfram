def main():
    max_width = 80 # Max width you wanna calculate to
    rule_num = 118 # Set the wolfram rule number

    row = [0]*1 + [1] + [0]*1
    print_row(row, max_width)
    while True:
        row = get_next_gen(row, rule_num)
        if len(row) - 2 >= max_width:
            return
        print_row(row, max_width)


# Get next generation of row
def get_next_gen(row, number):
    result_row = [0]*len(row)
    neighborhoods = get_neighborhood(row)
    for index, neighborhood in enumerate(neighborhoods):
        result_row[index] = enforce_rule(neighborhood[0], neighborhood[1], neighborhood[2], number)

    # Expand Result after each iteration
    result_row.insert(0, 0)
    result_row.insert(len(result_row), 0)
    return result_row


def enforce_rule(left, me, right, number):
    rules = wolfram_rule_generator(number)
    text = '%d%d%d' % (left, me, right)
    return int(rules[text])


# Return the all the neighborhood relates to the cell
def get_neighborhood(row):
    result = []
    for cell_num in range(len(row)):
        left = None
        if cell_num == 0:
            left = 0
        else:
            left = row[cell_num-1]
        me = row[cell_num]
        right = None
        if cell_num == len(row) - 1:
            right = 0
        else:
            right = row[cell_num +1]
        result.append([left, me, right])
    return result


def wolfram_rule_generator(number):
    # Find the rule set and translate it into binary and reverse it into rule order
    result_set = "{0:08b}".format(number)[::-1]
    rules = {}
    # Iterate thur all the possible combination
    for i in range(0, 8):
        rule = "{0:03b}".format(i)
        rules[rule] = result_set[i]
    return rules


# Print the row with white block and black block
def print_row(row, max_width):
    line = ''
    empty_cell = '\u25A1'
    full_cell = '\u25A0'
    for cell in row:
        if cell == 0:
            line += empty_cell
        else:
            line += full_cell
    line = '{0:{2}^{1}}'.format(line, max_width, empty_cell)
    print(line)


main()