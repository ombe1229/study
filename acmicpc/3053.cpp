#include <cmath>
#include <iostream>

using namespace std;

double r;

int main() {
  cin >> r;
  cout << fixed;
  cout.precision(6);
  cout << M_PI * pow(r, 2) << "\n" << 2 * pow(r, 2) << "\n";
  return 0;
}