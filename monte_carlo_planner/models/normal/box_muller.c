#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

void box_muller(double *z1, double *z2) {
    double u1 = (double)rand() / RAND_MAX;
    double u2 = (double)rand() / RAND_MAX;

    *z1 = sqrt(-2 * log(u1)) * cos(2 * M_PI * u2);
    *z2 = sqrt(-2 * log(u1)) * sin(2 * M_PI * u2);
}

int main() {
    // Seed the random number generator
    srand(time(NULL));

    double mu = 0;  // mean
    double sigma = 1;  // standard deviation

    double z1, z2;
    box_muller(&z1, &z2);

    double x1 = mu + z1 * sigma;
    double x2 = mu + z2 * sigma;

    printf("Generated numbers: x1 = %f, x2 = %f\n", x1, x2);

    return 0;
}
