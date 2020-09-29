#include <iostream>
using namespace std;
double fy(double x, double y, double z) {
	return (z - y) * x;
}
double fz(double x, double y, double z) {
	return (z + y) * x;
}
int main()
{
	double a = 0;
	double b = 1;
	double h = 0.1;
	double n = (b - a) / h;
	double x;
	double y[10];
	double z[10];
	y[0] = 1;
	z[0] = 1;
	for (int i = 0; i < n; i++) {
		x = i * h;
		y[i + 1] = y[i] + h * fy(x, y[i], z[i]);
		z[i + 1] = z[i] + h * fz(x, y[i], z[i]);
	}
	for (int i = 0; i < n; i++) {
		x = i * h;
		cout << " x[" << i << "]=" << x;
		cout << " y[" << i << "]=" << y[i];
		cout << " z[" << i << "]=" << z[i] << endl;
	}
}