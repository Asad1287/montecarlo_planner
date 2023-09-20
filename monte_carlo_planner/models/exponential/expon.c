#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <stdio.h>

double generate_two_param_exponential(double lambda, double beta) {
    // Generate a random number between 0 and 1
    double u = (double) rand() / (double) RAND_MAX;

    // Generate the exponentially-distributed number
    double x = beta - log(1 - u) / lambda;

    return x;
}

int main() {
    // Seed the random number generator
    srand(time(0));

    // Test the function
    double lambda = 1.0;  // Rate parameter for the exponential distribution
    double beta = 2.0;    // Location parameter for the exponential distribution
    double value = generate_two_param_exponential(lambda, beta);
    
    // Output the generated value
    printf("Generated Two-Parameter Exponential Number: %lf\n", value);

    return 0;
}
