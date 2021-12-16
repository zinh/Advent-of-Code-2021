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
  ifstream infile(filename);
  string line;
  int depth = 0;
  int horizon = 0;
  int aim = 0;
  while (getline(infile, line)) {
    istringstream iss(line);
    string command;
    int pos;
    iss >> command >> pos;
    if (command == "forward")
    {
      horizon += pos;
      depth += (aim * pos);
    }
    else if (command == "up")
      aim -= pos;
    else if (command == "down")
      aim += pos;
  }
  cout << depth * horizon << endl;
  return 0;
}
