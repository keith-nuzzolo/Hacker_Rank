/*
Sami's spaceship crashed on Mars!
She sends  sequential SOS messages to Earth for help.
Letters in some of the SOS messages are altered by cosmic radiation during transmission.
Given the signal received by Earth as a string,S,
determine how many letters of Sami's SOS have been changed by radiation.

Input Format
There is one line of input: a single string,S

Note: As the original message is just SOS repeated n times,
S's length will be a multiple of 3.

Constraints
1 <= |S| <= 99
|S|%3 = 0
S will contain only uppercase English letters.

Output Format

Print the number of letters in Sami's message that were altered by cosmic radiation.

Sample Input 0
SOSSPSSQSSOR

Sample Output 0
3
*/
#include <iostream>
using namespace std;


int main(){
  string s;
  cin >> s;
  int index  = 0;
  int replacements = 0;
  while (s[index] != '\0')
  {
    if (s[index] != "SOS"[index%3])
      replacements++;
    index++;
  }
  cout << replacements;
  return 0;
}
