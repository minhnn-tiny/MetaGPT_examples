from matrix import Matrix

def main():
    # Read the input matrix
    matrix = []
    for _ in range(int(input())):
        matrix.append([int(x) for x in input().split()])

    # Create a Matrix object
    matrix = Matrix(matrix)

    # Process queries
    for _ in range(int(input())):
        x, y = map(int, input().split())
        parity = matrix.get_parity(x, y)
        print(parity)

if __name__ == "__main__":
    main()
