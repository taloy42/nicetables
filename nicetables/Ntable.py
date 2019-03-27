

table = [
    ['Last name',   'First name',   'Age'],
    ['Smith',       'John',         30],
    ['Carpenter',   'Jack',         47],
    ['Johnson',     'Paul',         62],
]
from build_table_help import *

class nice_table(object):
    """docstring for nice_table"""

    def __init__(self, table):
        super(nice_table, self).__init__()
        self.table_arr = table
        self.rows_num = len(table)-1
        self.col_num = len(table[0])
        self.table_str = build_table(table)

    def __str__(self):
        return self.table_str

    def add_row(self, *values):
        if len(values)==1:
            val_arr=[]
            for item in values[0]:
                val_arr.append(item)
            self.table_arr.append(val_arr)
            self.table_str = build_table(self.table_arr)
        elif len(values) != self.col_num:
            raise ValueError("not enough values for the coloumn number")
        
        else:
            self.table_arr.append(values)
            self.table_str = build_table(self.table_arr)

    def update_row(self, col_n, col_v,*values ):
        col = build_col(self.table_arr, col_n)
        for i in range(len(col)):
            if col_v == col[i]:
                row_n = i
                break
        try:
            del self.table_arr[row_n]
            self.add_row(values)
        except NameError:
            print("no value was found")

    def del_row(self, col_n, col_v):
        col = build_col(self.table_arr, col_n)
        for i in range(len(col)):
            if col_v == col[i]:
                row_n = i
                break
        try:
            del self.table_arr[row_n]
        except NameError:
            print("no value was found")
    def add_coloumn(self, col_name, def_value):
        for row in range(len(self.table_arr)):
            self.table_arr[row].append(def_value)
        self.table_arr[0][len(self.table_arr[0])-1]=col_name
        self.table_str=build_table(self.table_arr)
    def show(self):
        print(t)


if __name__ == '__main__':
    print("Use The build_table(table) function")
    t = nice_table(table)
    print(t)
    t.add_row('Levi','Tal',20)
    t.update_row(0,'Levi', 'Levi', 'Tal',21)
