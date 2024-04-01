#include "set.h"

Set::Set() : elements() {}

void Set::add(int element) {
  elements.push_back(element);
}

void Set::erase(int element) {
  for (auto it = elements.begin(); it != elements.end(); ++it) {
    if (*it == element) {
      elements.erase(it);
      return;
    }
  }
}

int Set::sum() const {
  int sum = 0;
  for (auto element : elements) {
    sum += element;
  }
  return sum;
}
