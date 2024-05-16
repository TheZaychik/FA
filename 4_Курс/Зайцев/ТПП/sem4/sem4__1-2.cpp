
#include <iostream>
#include <stdio.h>
#include <iostream>
#include <omp.h>

using namespace std;
int main()
{
    setlocale(LC_ALL, "Russian");
    double k = 0;
    omp_set_nested(1);
    // max num_threads 2048
    omp_set_num_threads(2);
#pragma omp parallel 
#pragma omp parallel
#pragma omp parallel
    cout << omp_get_thread_num() << endl;

    return 0;
}
