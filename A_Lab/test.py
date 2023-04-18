def tape_needed(paper_size):
    return 2 ** (-5 / 4 + paper_size / 2)

def main():
    # Read input
    n = int(input().strip())
    papers = list(map(int, input().strip().split()))

    # Initialize variables
    total_tape = 0
    available_papers = [0] * (n + 1)
    needed_papers = 1

    # Convert papers into A1 size
    for paper_size in range(n, 1, -1):
        if paper_size - 2 < len(papers):
            available_papers[paper_size] = papers[paper_size - 2]

        while available_papers[paper_size] >= needed_papers:
            total_tape += tape_needed(paper_size) * needed_papers
            available_papers[paper_size] -= needed_papers
            needed_papers *= 2
            paper_size -= 1

    # Check if there are enough papers to make an A1 paper
    if available_papers[1] >= needed_papers:
        total_tape += tape_needed(1) * needed_papers
        print(total_tape)
    else:
        print("impossible")

if __name__ == "__main__":
    main()
