#include <iostream>
#include <vector>

using namespace std;

long long minn, maxx;
int cnt;

int main() {
  cin >> minn >> maxx;
  vector<bool> vec(maxx - minn + 1, false);

  for (long long i = 2; i * i <= maxx; i++) {
    long long n = minn / (i * i);
    if (minn % (i * i)) n++;
    while (n * i * i <= maxx) {
      vec[n * i * i - minn] = true;
      n++;
    }
  }

  cnt = 0;
  for (int i = 0; i <= maxx - minn; i++) {
    if (vec[i] == 0) cnt++;
  }
  cout << cnt << "\n";
  return 0;
}