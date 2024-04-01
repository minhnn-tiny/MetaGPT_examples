import sys
from typing import List

class Plan:
    def __init__(self, months: int, rate: float, cost: int):
        self.months = months
        self.rate = rate
        self.cost = cost

    def get_total_cost(self, minutes: int) -> float:
        return self.cost + (minutes * self.rate)


class Solution:
    def __init__(self, default_rate: float, minutes: int, plans: List[Plan]):
        self.default_rate = default_rate
        self.minutes = minutes
        self.plans = plans

    def solve(self) -> int:
        best_plan = None
        best_cost = float('inf')
        for plan in self.plans:
            total_cost = plan.get_total_cost(self.minutes)
            if total_cost < best_cost:
                best_plan = plan
                best_cost = total_cost

        if best_cost < self.default_rate * self.minutes:
            return self.plans.index(best_plan) + 1
        else:
            return 0


def main():
    default_rate = float(sys.stdin.readline())
    minutes = int(sys.stdin.readline())
    num_plans = int(sys.stdin.readline())
    plans = []
    for _ in range(num_plans):
        months, rate, cost = map(int, sys.stdin.readline().split())
        plans.append(Plan(months, rate, cost))

    solution = Solution(default_rate, minutes, plans)
    result = solution.solve()
    print(result)


if __name__ == "__main__":
    main()
