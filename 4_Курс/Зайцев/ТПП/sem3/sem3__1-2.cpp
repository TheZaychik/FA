#include <iostream>
#include "omp.h"
#include <string>
#include <locale>
#include <vector>

using namespace std;
int main()
{
	setlocale(LC_ALL, "Russian");
	int x = 0;
	vector<float> vector1(100000000);
	vector<float> vector2(100000000);
	vector<float> vectorR(100000000);
	int t = clock();
	for (int i = 0; i < 100000000; i++)
	{
		vector1[i] = static_cast<float>(rand()) / static_cast<float>(RAND_MAX);
	}
	for (int i = 0; i < 100000000; i++)
	{
		vector2[i] = static_cast<float>(rand()) / static_cast<float>(RAND_MAX);
	}
	for (int i = 0; i < 100000000; i++)
	{
		vectorR[i] = vector1[i] + vector2[i];
	}
	cout << "Размер vectorR " << vectorR.size() << ", его 5000й элемент равен " << vectorR[5000] << endl;
	t = clock() - t;
	cout << "Время сложения векторов в однопоточном режиме " << t / CLOCKS_PER_SEC << " секунд" << endl;
	cout << endl;
	t = clock();
#pragma omp parallel
	{
#pragma omp parallel for
		for (int i = 0; i < 100000000; i++)
		{
			vector1[i] = static_cast<float>(rand()) / static_cast<float>(RAND_MAX);
		}
#pragma omp parallel for
		for (int i = 0; i < 100000000; i++)
		{
			vector2[i] = static_cast<float>(rand()) / static_cast<float>(RAND_MAX);
		}
#pragma omp barrier
#pragma omp parallel for
		for (int i = 0; i < 100000000; i++)
		{
			vectorR[i] = vector1[i] + vector2[i];
		}
	}
	cout << "Размер vectorR " << vectorR.size() << ", его 5000й элемент равен " << vectorR[5000] << endl;
	t = clock() - t;
	cout << "Время сложения векторов в параллельном режиме " << t / CLOCKS_PER_SEC << " секунд" << endl;
	return 0;
}
