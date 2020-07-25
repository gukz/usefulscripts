def find(arr):
    axb = 0
    for a in arr:
        axb ^= a
    single_bit = 1
    while axb & sin


if __name__ == "__main__":
    assert set(find([2, 3, 1, 1, 4, 4, 5, 5, 6, 6])) == {2, 3}
