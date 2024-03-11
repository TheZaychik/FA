#include <stdio.h>
#include <omp.h>
#include <locale>
int main()
{
    setlocale(LC_ALL, "Russian");
    int n;
    omp_set_num_threads(3);
    omp_set_nested(1); // разрешаем использование вложенных параллельных областей - устанавливаем переменную окружения
#pragma omp parallel private(n)
    {
        n = omp_get_thread_num(); // определение номера потока во внешней параллельной секции
        printf("Внешняя параллельная секция 1, поток n=%d \n", n);
#pragma omp parallel
        {
            printf("Вложенная параллельная секция 1, поток %d - %d\n", n, omp_get_thread_num());
        }
    }
    omp_set_nested(0); // запрещаем использование вложенных параллельных областей - сбрасываем переменную окружения
#pragma omp parallel private(n)
    {
        n = omp_get_thread_num();
        printf("Внешняя параллельная секция 2, поток n=%d \n", n);
#pragma omp parallel
        {
            printf("Вложенная параллельная секция 2, поток %d - %d\n", n,
                   omp_get_thread_num());
        }
    }
    return 0;
}
