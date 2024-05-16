#include <stdio.h>
#include <omp.h>

int main()
{
    int total = 0;
    int NMAX = 100;
    int sum;
    int a[100][100];
    int b[100][100];
#pragma omp parallel shared(a, b) private(i, j)
    {
#pragma omp sections /* Вычисление сумм элементов строк и общей суммы */
        {
            for (int i = 0; i < NMAX; i++)
            {
                sum = 0;
                for (int j = i; j < NMAX; j++)
                    sum += a[i][j];
                printf("Сумма элементов строки %d равна %d\n", i, sum);
                total = total + sum;
            }
#pragma omp section
            {
                /* Копирование матрицы */
                for (int i = 0; i < NMAX; i++)
                {
                    for (int j = i; j < NMAX; j++)
                        b[i][j] = a[i][j];
                }
            } /* Завершение параллельного фрагмента */
        }
        printf("Общая сумма элементов матрицы равна %d\n", total);
    }
}