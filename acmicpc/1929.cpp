// https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

#include <string.h>

#include <cmath>
#include <iostream>

using namespace std;

int n, m;

int main(void) {
  cin >> m >> n;
  bool* arr = new bool[n + 1];
  memset(arr, true, n + 1);
  arr[0] = false;
  arr[1] = false;
  for (int i = 2; i <= sqrt(n); i++) {
    if (arr[i]) {
      for (int j = i * 2; j <= n; j += i) {
        arr[j] = false;
      }
    }
  }

  for (int i = m; i <= n; i++) {
    if (arr[i]) cout << i << "\n";
    // https://www.educative.io/edpresso/what-is-the-difference-between-endl-and-n-in-cpp
  }
  return 0;
}