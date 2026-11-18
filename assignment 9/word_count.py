
def main():
    filename = input("Enter the name of the input file: ")

    try:
        with open(filename, "r") as infile:
            words = infile.read().split()

        word_counts = {}

        # Count each word
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

        # Display the word counts
        print(f"{'Word':<20}{'Occurrences'}")
        print("-" * 45)

        for word, count in word_counts.items():
            print(f"{word:<20}{count}")

    except FileNotFoundError:
        print("Error: The file could not be found.")


if __name__ == "__main__":
    main()
