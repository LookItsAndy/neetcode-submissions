# Paste your solution() function above this line, or import it.
from submission_0 import solution


def run_test(matrix, expected_weights, label):
    print(f"--- {label} ---")
    print("matrix:")
    for r in matrix:
        print(" ", r)

    keys = solution(matrix)  # whatever your function currently returns
    print("your output:", keys)
    print("expected weights (key -> weight):", expected_weights)
    print()


if __name__ == "__main__":
    matrix_4x4 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    # hand-traced weights: 1->34, 5->26, 9->26, 13->34
    expected_4x4 = {1: 34, 5: 26, 9: 26, 13: 34}
    run_test(matrix_4x4, expected_4x4, "4x4 (has a tie: 34 and 26 each appear twice)")

    # single row/col edge case
    matrix_1x1 = [[7]]
    expected_1x1 = {7: 7}
    run_test(matrix_1x1, expected_1x1, "1x1 edge case")

    # 2x2, small enough to trace fully by hand yourself
    matrix_2x2 = [
        [1, 2],
        [3, 4],
    ]
    run_test(matrix_2x2, {}, "2x2 (trace this one yourself before checking)")