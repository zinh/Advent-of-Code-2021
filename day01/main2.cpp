#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;
int main(int argc, char **argv) {
  if (argc < 2) {
    cout << "Need a filename" << endl;
    cout << "Syntax: main FILENAME" << endl;
    return 1;
  }

  char *filename = argv[1];
  std::ifstream infile(filename);
  string line;
  vector<int> lst;
  while (getline(infile, line)) {
    istringstream iss(line);
    int current_measurement;
    if (!(iss >> current_measurement)) {
      cout << "Error parsing line: " << line << endl;
      return 1;
    }
    lst.push_back(current_measurement);
  }
  vector<int> v1(lst.begin(), lst.end() - 2);
  vector<int> v2(lst.begin() + 1, lst.end() - 1);
  vector<int> v3(lst.begin() + 2, lst.end());
  int previous_sum = 100000;
  int count = 0;
  for (auto& el : v1) {
    auto idx = &el - &v1[0];
    auto sum = el + v2[idx] + v3[idx];
    if (sum > previous_sum)
      count++;
    previous_sum = sum;
  }

  cout << count << endl;
  return 0;
}
