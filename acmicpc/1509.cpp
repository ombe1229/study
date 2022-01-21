#include <iostream>

using namespace std;

string text;
bool palindrome[2510][2510];
int dp[2510];

int main(void) {
  cin >> text;
  text = " " + text;
  int n = text.length();
  for (int i = 0; i <= n; i++) palindrome[i][i] = true;
  for (int i = 0; i < n; i++) palindrome[i][i + 1] = (text[i] == text[i + 1]);

  for (int i = 2; i < n; i++) {
    for (int j = 1; j <= n - i; j++) {
      if (text[j] == text[i + j] && palindrome[j + 1][j + i - 1])
        palindrome[j][j + i] = 1;
    }
  }

  for (int i = 1; i < n; i++) {
    dp[i] = 1e9;
    for (int j = 1; j <= i; j++) {
      if (palindrome[j][i]) dp[i] = min(dp[i], dp[j - 1] + 1);
    }
  }

  cout << dp[n - 1] << endl;

  return 0;
}
