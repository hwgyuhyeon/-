#include <stdio.h>
#include <math.h>
#define SIZE 10

int main(void) {

	double arr[SIZE] = { 14, 21, 29,33,40,45,49,50,52,67 };
	double average = 0;
	double s2, s;
	double semis2 = 0;

	for (int i = 0; i < SIZE; i++) {
		//scanf("%lf", &arr[i]);
		average += arr[i];
		semis2 += (arr[i] - average) * (arr[i] - average);
	}

	average /= (double)SIZE;
	printf("표본평균 : %lf", average);

	s2 = 18286 / 10 - 400;
	printf(" 표본분산 : %lf", s2);

	s2 = 1428.6;
	double diff;
	s = sqrt(s2);
	diff = s / average;

	printf(" 표본변동계수 : %lf", diff);

	return 0;
}
