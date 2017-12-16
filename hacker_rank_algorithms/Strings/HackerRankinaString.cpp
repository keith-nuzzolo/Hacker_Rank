/*
We say that a string, s, contains the word hackerrank if a subsequence of the
characters in  spell the word hackerrank.
For example, haacckkerrannkk does contain hackerrank, but haacckkerannk does not
(the characters all appear in the same order, but it's missing a second r).

More formally, let p0, p1,..., p9 be the respective indices of
h, a, c, k, e, r, r, a, n, k in string s. If p0 < p1 < p2 < ... < p9 is true,
then s contains hackerrank.

You must answer q queries, where each query consists of a string, s.
For each query, print YES on a new line if contains hackerrank;
otherwise, print NO instead.

Input Format

The first line contains an integer denoting q (the number of queries).
Each line of the q subsequent lines contains a single string denoting s.

Constraints
2 <= q <= 10^2
10 <= length(s) <= 10^4

Output Format
For each query, print YES on a new line if  contains hackerrank; otherwise,
print NO instead.

Sample Input 0

2
hereiamstackerrank
hackerworld
Sample Output 0

YES
NO
*/
using namespace std;

int main() {
  int q;
  cin >> q;
  string t[q];
  for(int i = 0; i < q; i++)
    cin >> t[i];
  for(int i = 0; i < q; i++)
  {
    string comp = "hackerrank";
    int index = 0;
    for(int c = 0; c < t[i].length(); c++){
      if(t[i][c] == comp[index])
        index++;
    }
    if(index == comp.length())
      cout << "YES\n";
    else
      cout << "NO\n";
  }
  return 0;
}
