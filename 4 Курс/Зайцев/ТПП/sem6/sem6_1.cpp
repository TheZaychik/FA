#include <iostream>
#include <stdio.h>
#include <omp.h>
#include <locale>
#include <unistd.h>

using namespace std;
int main()
{

	int i;
	double time = omp_get_wtime();
#pragma omp parallel private(i) num_threads(4)
	{
// #pragma omp for schedule (static, 6)
#pragma omp for schedule (dynamic, 6)
//#pragma omp for schedule (guided, 6)
//#pragma omp for schedule (auto)
//#pragma omp for schedule (runtime)
		for (i = 0; i<200; i++)
		{
			printf("Поток %d выполнила итерацию %d\n", omp_get_thread_num(), i);
			usleep(1000); 
		}
	}
	cout << "Time = " << (omp_get_wtime() - time) << endl;
}
