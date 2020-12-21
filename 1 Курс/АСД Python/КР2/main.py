import replace_Zaytsev
import totext_Zaytsev
import v2_1


def main():
    replace_Zaytsev.save_table('text1.txt', replace_Zaytsev.main('text1.txt', 'replace.csv'))
    print(v2_1.cummulate(1, 3, 2, 2, mul=True))
    totext_Zaytsev.totext(totext_Zaytsev.csv_reader('csv.csv'), 'csv.text')


if __name__ == '__main__':
    main()