#include <iostream>
#include "set.h"

int main() {
  Set set;
  int n;
  std::cin >> n;
  for (int i = 0; i < n; i++) {
    int x;
    std::cin >> x;
    set.add(x);
  }
  std::cout << set.sum() << std::endl;
  return 0;
}
