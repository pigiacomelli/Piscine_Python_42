import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    scores: list[int] = []

    
    for arg in sys.argv[1:]:
        try:
            value = int(arg)
            scores.append(value)
        except ValueError:
            print(f"Invalid score ignored: {arg}")

    
    if len(scores) == 0:
        print("No valid scores to process.")
        return

    total_players: int = len(scores)
    total_score: int = sum(scores)
    average_score: int = total_score / total_players
    high_score: int = max(scores)
    low_score: int = min(scores)
    score_range: int = high_score - low_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
