class Solution:
    def count_valid_fours(self, A: str, B: str, K: int) -> int:
        count = 0
        for i in range(len(A) - K + 1):
            for j in range(len(B) - K + 1):
                if self.hamming_distance(A[i:i + K], B[j:j + K]) <= K:
                    count += 1
        return count

    def hamming_distance(self, A: str, B: str) -> int:
        distance = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                distance += 1
        return distance
