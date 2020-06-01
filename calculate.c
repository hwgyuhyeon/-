#include <stdio.h>
#include <math.h>
#define SIZE 10

int main(void) {

	double arr[SIZE] = { 0 };
	double average = 0, sqrave = 0;
	double s2, s;

	for (int i = 0; i < SIZE; i++) {
		scanf("%lf", &arr[i]);
		average += arr[i];
		sqrave += arr[i] * arr[i];
	}

	average /= (double)SIZE;
	sqrave /= (double)SIZE;
	printf("평균 : %lf", average);

	s2 = sqrave - average * average;
	printf("분산 : %lf", s2);

	s = sqrt(s2);
	printf("표준편차 : %lf", s);

	return 0;
}

//수정수정맨~
