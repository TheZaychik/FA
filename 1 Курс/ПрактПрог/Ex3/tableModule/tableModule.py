import csv
import pickle
import copy
import os

'''
tableModule by Kroll 
Table provided as dictionary (columns) in list (rows)
--
4) + Реализовать автоматическое определение типа столбцов по хранящимся в таблице значениям. 
Оформить как отдельную функцию и встроить этот функционал как опцию работы функции load_table.
Сложность 1 или 2

6) + Добавить набор функций add, sub, mul, div, которые обеспечат выполнение арифмитических 
операций для столбцов типа int, float, bool. Продумать сигнатуру функций и изменения в 
другие функции, которые позволят удобно выполнять арифметические операции со столбцами и присваивать результаты выч. 
Реализовать реагирование на некорректные значения с помощью генерации исключительных ситуаций.
Сложность 2

8) + Реализовать функцию merge_tables(table1, table2, by_number=True): в результате слияния создается таблица с 
набором столбцов, соответствующих объединенному набору столбцов исходных таблиц. Соответствие строк ищется либо по их номеру 
(by_number=True) либо по значению индекса (1й столбец). При выполнении слияния возможно множество конфликтных ситуаций. 
Автор должен их описать и определить допустимый 
способ реакции на них (в т.ч. через дополнительные параметры функции и инициацию исключительных ситуаций).
Сложность 2

3) + Реализовать функцию concat(table1, table2) и split(row_number) склеивающую две таблицы или 
разбивающую одну таблицу на 2 по номеру строки. 
Сложность 1
'''


class Table:
    def __init__(self, filename='', table=None, delimiter_csv=';'):
        self.table = []
        if table:
            self.table = copy.deepcopy(table)
            return
        if not os.path.exists(filename):
            raise FileNotFoundError
        if '.csv' in filename:
            with open(filename) as f_obj:
                reader = csv.DictReader(f_obj, delimiter=delimiter_csv)
                for line in reader:
                    self.table.append(line)
        elif '.pickle' in filename:
            with open(filename, 'rb') as f_obj:
                unpickler = pickle.Unpickler(f_obj)
                self.table = unpickler.load()
        else:
            raise Exception('Unknown file extension')
        for row in self.table:
            for k in row.keys():
                if (type(row[k]) != int) and row[k].isdigit():
                    row[k] = int(row[k])

        print('Imported table:\n', self.table)

    def __str__(self):
        return str(self.table)

    def __check_rows(self, row):
        if type(row) != int:
            raise TypeError('Row variable is not int')
        if row >= len(self.table) or row <= -1:
            raise Exception('Not correct row selected')

    def __check_column(self, column):
        if type(column) != int:
            raise TypeError('Column variable is not int')
        if column >= len(self.table[0].keys()) or column <= -1:
            raise Exception('Not correct column selected')

    def __check_bool(self, bool_variable, name):
        if (bool_variable <= -1 or bool_variable >= 2) and type(bool_variable) != bool:
            raise TypeError(name + ' variable more than 2 or not bool')

    def save_table(self, filename, delimiter_csv=';'):
        if '.csv' in filename:
            with open(filename, "w", newline='') as f_obj:
                fieldnames = self.table[0].keys()
                writer = csv.DictWriter(f_obj, delimiter=delimiter_csv, fieldnames=fieldnames)
                writer.writeheader()
                for row in self.table:
                    writer.writerow(row)
        elif '.pickle' in filename:
            with open('data.pickle', 'wb') as f_obj:
                pickle.dump(self.table, f_obj)
        else:
            raise Exception('Unknown file extension')
        print('Saved table:\n', self.table)
        print('Saved at', filename)

    def add(self, row, col, value):
        try:
            self.table[row][col] += value
        except Exception as e:
            print(e)

    def sub(self, row, col, value):
        try:
            self.table[row][col] -= value
        except Exception as e:
            print(e)

    def mul(self, row, col, value):
        try:
            self.table[row][col] %= value
        except Exception as e:
            print(e)

    def div(self, row, col, value):
        try:
            self.table[row][col] //= value
        except Exception as e:
            print(e)

    def merge_tables(self, table, by_number=True):
        keys = list(self.table[0].keys())
        for key in table[0].keys():
            if key not in keys:
                keys.append(key)
        print(keys)
        for row1, row2 in zip(self.table, table):
            for key1, key2 in zip(list(row1.keys()), list(row2.keys())):
                if key1 != key2:
                    row1[key2] = row2[key2]
        print(self.table)

    def get_rows_by_number(self, start, stop=None, copy_table=False):
        if type(start) != int:
            raise TypeError('Start variable not int')
        self.__check_bool(copy_table, 'Copy_table')

        table = []
        if stop:
            if type(stop) != int:
                raise TypeError('Stop variable is not int')
            table = self.table[start:stop]
        else:
            table.append(self.table[start])
        if copy_table:
            table = copy.deepcopy(table)
        return Table(table=table)

    def split(self, row_number):
        self.__check_rows(row_number)

        table = self.table[row_number:]
        self.table = copy.deepcopy(self.table[:row_number])
        return Table(table=table)

    def concat(self, table):
        if table[0].keys() != self.table[0].keys():
            raise KeyError('No correct key in provided table!')
        self.table.append(table)

    def get_rows_by_index(self, *index, copy_table=False):
        self.__check_bool(copy_table, 'Copy_table')

        table = []
        for i in index:
            for row in self.table:
                key = list(row.keys())[0]
                print(row[key], i)
                if str(row[key]) == str(i):
                    table.append(row)
        if copy_table:
            table = copy.deepcopy(table)
        return Table(table=table)

    def get_column_types(self, by_number=True):
        self.__check_bool(by_number, 'By_number')

        table = []
        for i in range(len(self.table)):
            table.append({})
            keys = self.table[i].keys()
            for k in keys:
                if by_number:
                    table[i][list(keys).index(k)] = type(self.table[i][k])
                else:
                    table[i][k] = type(self.table[i][k])
        return Table(table=table)

    def set_column_types(self, types_dict, by_number=True):
        if len(types_dict.keys()) != len(self.table[0].keys()):
            raise Exception('Not equal length between dicts')
        self.__check_bool(by_number, 'By_number')

        for i in range(len(self.table)):
            keys_td = types_dict.keys()
            keys = self.table[i].keys()
            for k in keys_td:
                if by_number:
                    self.table[i][list(keys)[k]] = types_dict[k](self.table[i][list(keys)[k]])
                else:
                    self.table[i][k] = types_dict[k](self.table[i][k])

    def get_values(self, column=0):
        self.__check_column(column)

        table = []
        for i in range(len(self.table)):
            table.append({})
            key = list(self.table[i].keys())[column]
            table[i][key] = self.table[i][key]
        return Table(table=table)

    def get_value(self, column=0):
        self.__check_column(column)

        table = [{}]
        key = list(self.table[0].keys())[column]
        table[0][key] = self.table[0][key]
        return Table(table=table)

    def set_values(self, *values, column=0):
        self.__check_column(column)

        for i in range(len(values)):
            key = list(self.table[i].keys())[column]
            self.table[i][key] = values[i]

    def set_value(self, value, column=0):
        self.__check_column(column)

        key = list(self.table[0].keys())[column]
        self.table[0][key] = value

    def print_table(self):
        print(self.table)


def test():
    a = Table('/Users/nikitazaytsev/git/FA/1 Курс/ПрактПрог/Ex3/data.csv')
    t = Table('/Users/nikitazaytsev/git/FA/1 Курс/ПрактПрог/Ex3/data1.csv')
    a.merge_tables(t.table)


if __name__ == '__main__':
    test()
