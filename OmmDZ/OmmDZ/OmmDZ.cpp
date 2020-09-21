#include <iostream>
#include <cmath>
using namespace std;
double f1(double x, double y) {
	return 2 * x * pow(y, 3) / (1 - pow(x, 2) * pow(y, 2));
}
int main()
{
	double a = 2;
	double b = 2.5;
	double h = 0.05;
	double n = (b - a) / h;
	double x, y = 1;
	for (int i = 0; i <= n; i++) {
		x = a + i * h;
		cout << "   x[" << i << "]=" << x;
		cout << "   y[" << i << "]=" << y << endl;
		y = y + h * f1(x, y);

	}

}
