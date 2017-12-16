/*
Roy wanted to increase his typing speed for programming contests.
So, his friend advised him to type the sentence
"The quick brown fox jumps over the lazy dog" repeatedly, because it is a pangram.
(Pangrams are sentences constructed by using every letter of the alphabet at least once.)

After typing the sentence several times, Roy became bored with it.
So he started to look for other pangrams.

Given a sentence , tell Roy if it is a pangram or not.

Input Format
Input consists of a string s.

Constraints
Length of s can be at most 10^3(1 <= |s| <= 10^3) and it may contain spaces,
lower case and upper case letters.
Lower-case and upper-case instances of a letter are considered the same.

Output Format
Output a line containing pangram if  is a pangram, otherwise output not pangram.

Sample Input
Input #1
We promptly judged antique ivory buckles for the next prize

Input #2
We promptly judged antique ivory buckles for the prize

Sample Output
Output #1
pangram

Output #2
not pangram
*/
#include <iostream>
#include <set>
using namespace std;


int main() {
  string q;
  getline(cin, q);
  set<char> s;
  int index = 0;
  while(q[index] != '\0')
  {
    int a = tolower(q[index]);
    if((a >= 'a' and a <= 'z'))
      s.insert(tolower(q[index]));
    index++;
  }
  if( s.size() != 26)
    cout << "not ";
  cout << "pangram";

  return 0;

}
