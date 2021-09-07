import csv
import pickle
from Ex3.tableModule import tableModule


def main():
    a = tableModule.Table('/Users/nikitazaytsev/git/FA/1 Курс/ПрактПрог/Ex3/data.csv')
    b = tableModule.Table('/Users/nikitazaytsev/git/FA/1 Курс/ПрактПрог/Ex3/data1.csv')
    a.merge_tables(b.table)
    a.save_table('data3.pickle')



if __name__ == '__main__':
    main()
