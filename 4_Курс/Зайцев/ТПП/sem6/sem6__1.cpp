#include <iostream>
#include <stdio.h>
#include <omp.h>
#include <locale>
#include <unistd.h>

using namespace std;
int main()
{

	int i;
	int sum = 0;
	double time = omp_get_wtime();
#pragma omp parallel private(i) num_threads(4)
	{
#pragma omp for schedule(dynamic, 6) reduction(+ : sum)
		for (i = 0; i < 200; i++)
		{

			sum += i;
			printf("Поток %d выполнила итерацию %d\n", omp_get_thread_num(), i);
			printf("Сумма: %d\n", sum);
			usleep(1000);
		}
	}
	printf("Итого: %d\n", sum);
}
