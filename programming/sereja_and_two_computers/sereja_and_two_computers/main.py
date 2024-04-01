from typing import List, Tuple

class Program:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __lt__(self, other: 'Program') -> bool:
        return self.a < other.a

class Solution:
    def __init__(self, programs: List[Program]):
        self.programs = programs
        self.optimal_time = 0
        self.start_times = []

    def solve(self) -> Tuple[int, List[Tuple[int, int]]]:
        self.programs.sort()

        for program in self.programs:
            start_time_on_second_computer = max(self.optimal_time, program.b)
            self.optimal_time = start_time_on_second_computer + program.a
            self.start_times.append((start_time_on_second_computer, start_time_on_second_computer + program.a))

        return self.optimal_time, self.start_times

def main():
    programs = [Program(2, 3), Program(1, 4), Program(3, 2)]
    solution = Solution(programs)
    optimal_time, start_times = solution.solve()
    print(optimal_time)
    print(start_times)

if __name__ == "__main__":
    main()
