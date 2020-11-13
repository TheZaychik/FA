import csv
import pickle
from Ex3.tableModule import tableModule


def main():
    a = tableModule.Table('/Users/nikitazaytsev/git/FA/1 Курс/ПрактПрог/Ex3/data.csv')
    b = a.get_rows_by_number(0, 3, copy_table=False)
    b.set_value(999, 0)
    print(a)
    print(b)


if __name__ == '__main__':
    main()
