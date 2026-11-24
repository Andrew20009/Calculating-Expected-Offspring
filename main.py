def read_info_from_txt(file_path: str) -> tuple[int, int, int, int, int, int]: # Reads the six couple counts in order AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa
    with open(file_path) as f: # Open the file for reading
        n1, n2, n3, n4, n5, n6 = map(int, f.read().split()) # Read file, split into 6 integers
    return n1, n2, n3, n4, n5, n6


def expected_offspring(n1: int, n2: int, n3: int, n4: int, n5: int, n6: int) -> float: # Returns the expected number of offspring with the dominant phenotype
    dominant = n1 * 1.00  # AA×AA couples, 100% dominant offspring
    dominant += n2 * 1.00 # AA×Aa couples, 100% dominant offspring
    dominant += n3 * 1.00 # AA×aa couples, 100% dominant offspring
    dominant += n4 * 0.75 # Aa×Aa couples, 75% dominant offspring
    dominant += n5 * 0.50 # Aa×aa couples, 50% dominant offspring
    dominant += n6 * 0.00 # aa×aa couples, 0% dominant offspring

    return dominant * 2 # Every couple has exactly two offspring, so multiply the sum by 2


if __name__ == "__main__": # Entry point of the code
    n1, n2, n3, n4, n5, n6 = read_info_from_txt("rosalind_iev.txt")
    result = expected_offspring(n1, n2, n3, n4, n5, n6)
    print(result)
