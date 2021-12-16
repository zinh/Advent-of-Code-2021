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
  int d = 0;
  int h = 0;
  while (getline(infile, line)) {
    istringstream iss(line);
    string command;
    int pos;
    iss >> command >> pos;
    if (command == "forward")
      h += pos;
    else if (command == "up")
      d -= pos;
    else if (command == "down")
      d += pos;
  }
  cout << d * h << endl;
  return 0;
}
