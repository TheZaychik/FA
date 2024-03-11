#include <stdio.h>
#include <omp.h>
#include <locale>

int main()
{
	setlocale(LC_ALL, "Russian");
	int i, n, j;
#pragma omp parallel private (i, n)
	{
		n = omp_get_thread_num();
#pragma omp for collapse(2)
		for (i = 0; i<10; i++)
			for (j = 0; j < 100; j++)
			{
				printf("Поток %d, итерация %d-%d\n", n, i, j);
			}
	}
}
