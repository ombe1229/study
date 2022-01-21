#include <iostream>

using namespace std;

int n, current, c;

int main(void) {
  cin >> n;
  current = n;
  c = 0;

  do {
    current = (current % 10) * 10 + ((current / 10) + (current % 10)) % 10;
    c++;
  } while (current != n);

  cout << c << endl;

  return 0;
}