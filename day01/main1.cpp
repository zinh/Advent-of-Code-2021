#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

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
  int previous_measurement = 100000;
  int result = 0;
  while (getline(infile, line)) {
    istringstream iss(line);
    int current_measurement;
    if (!(iss >> current_measurement)) {
      cout << "Error parsing line: " << line << endl;
      return 1;
    }
    if (current_measurement > previous_measurement)
      result++;

    previous_measurement = current_measurement;
  }
  cout << result << endl;
  return 0;
}
