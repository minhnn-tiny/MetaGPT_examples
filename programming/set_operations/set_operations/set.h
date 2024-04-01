#ifndef SET_H
#define SET_H

#include <vector>

class Set {
public:
  Set();
  void add(int element);
  void erase(int element);
  int sum() const;

private:
  std::vector<int> elements;
};

#endif  // SET_H
