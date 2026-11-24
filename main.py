"""Office Joke entry: write one line of office comedy to /output/entry.txt."""

import os

JOKE = "The printer only jams when it senses confidence, so I've started submitting documents in a self-doubting font."


def main():
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise ValueError("joke must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
