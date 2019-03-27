def table_check(table):
    # INPUT : table
    # OUTPUT : raises an error if not all rows have the same number of values
    row_before = table[0]

    for row in table:
        if len(row) != len(row_before):
            raise ValueError('not all rows have the same number of values')
            break
        else:
            row_before = row

def complete_spaces(string, length):
    spaces = length-len(string)
    spaces_bef = spaces//2
    if spaces % 2 == 0:
        return spaces_bef, spaces_bef
    else:
        return spaces_bef, spaces_bef+1


def build_col(table, col_num):
    col = []
    for row in table:
        col.append(row[col_num])
    return col


def max_length_in_col(col):
    max_len = len(col[0])
    for item in col:
        if len(str(item)) > max_len:
            max_len = len(str(item))
    return max_len


def col_max_arr(table):
    max_arr = []
    for col_num in range(len(table[0])):
        cur_col = build_col(table, col_num)
        cur_length = max_length_in_col(cur_col)
        max_arr.append(cur_length)
    return max_arr


def build_table(table):
    table_check(table)

    max_arr = col_max_arr(table)
    table_str = ''
    limit = '+'
    for max in max_arr:
        limit += (max+2)*'-'
        limit += '+'
    limit += '\n'
    table_str += limit

    for row in table:
        col_num = 0
        for item in row:
            before, after = complete_spaces(str(item), max_arr[col_num]+2)
            col_num += 1
            table_str += ('|'+' '*after)
            table_str += (str(item)+' '*before)
        table_str += '|\n'
        table_str += limit

    return table_str
