#include <stdio.h>
#include <omp.h>
#include <locale>

int main()
{
	setlocale(LC_ALL, "Russian");
	int i, n;
#pragma omp parallel private (i, n)
	{
		n = omp_get_thread_num();
#pragma omp for nowait
		for (i = 0; i<10; i++)
		{
			printf("Поток %d, итерация %d\n", n, i);
		}
	}
}
