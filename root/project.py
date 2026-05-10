import csv
import sys
from math import comb

SIDES = 6


def get_sum_distribution(num_dice):
    dist = {face: 1 for face in range(1, SIDES + 1)}
    for _ in range(num_dice - 1):
        new_dist = {}
        for s, count in dist.items():
            for face in range(1, SIDES + 1):
                new_dist[s + face] = new_dist.get(s + face, 0) + count
        dist = new_dist
    total = SIDES ** num_dice
    return {s: count / total for s, count in sorted(dist.items())}

def calculate_sum_probability(num_dice, num_throws, target):
    dist = get_sum_distribution(num_dice)
    p_once = dist.get(target, 0)
    p_atleast = 1 - (1 - p_once) ** num_throws
    return p_once, p_atleast

def sum_probability():
    num_dice   = int(input("Enter number of dice: "))
    num_throws = int(input("Enter number of throws: "))
    target     = int(input(f"Enter target sum ({num_dice} to {num_dice * SIDES}): "))

    p_once, p_atleast = calculate_sum_probability(num_dice, num_throws, target)

    print(f"Probability per throw       : {p_once * 100:.4f}%")
    print(f"Probability at least once   : {p_atleast * 100:.4f}%")


def at_least_success(num_dice, num_throws, threshold, min_k):
    dist = get_sum_distribution(num_dice)
    p    = sum(prob for s, prob in dist.items() if s >= threshold)

    prob = sum(
        comb(num_throws, k) * (p ** k) * ((1 - p) ** (num_throws - k))
        for k in range(min_k, num_throws + 1)
    )
    return prob

def at_least_success_interactive():
    num_dice   = int(input("Enter number of dice: "))
    num_throws = int(input("Enter number of throws: "))
    threshold  = int(input(f"Enter success value (sum >= ?, range {num_dice}-{num_dice * SIDES}): "))
    min_k      = int(input("Enter minimum number of successes: "))

    prob = at_least_success(num_dice, num_throws, threshold, min_k)
    print(f"Probability of at least {min_k} success(es): {prob * 100:.4f}%")


def at_most_success(num_dice, num_throws, threshold, max_k):
    dist = get_sum_distribution(num_dice)
    p    = sum(prob for s, prob in dist.items() if s >= threshold)

    prob = sum(
        comb(num_throws, k) * (p ** k) * ((1 - p) ** (num_throws - k))
        for k in range(0, max_k + 1)
    )
    return prob

def at_most_success_interactive():
    num_dice   = int(input("Enter number of dice: "))
    num_throws = int(input("Enter number of throws: "))
    threshold  = int(input(f"Enter success value (sum >= ?, range {num_dice}-{num_dice * SIDES}): "))
    max_k      = int(input("Enter maximum number of successes: "))

    prob = at_most_success(num_dice, num_throws, threshold, max_k)
    print(f"Probability of at most {max_k} success(es): {prob * 100:.4f}%")


def all_possible_sums():
    num_dice   = int(input("Enter number of dice: "))
    num_throws = int(input("Enter number of throws: "))
    filename   = input("Enter output filename (default: sums.csv): ").strip() or "sums.csv"

    dist  = get_sum_distribution(num_dice)
    total = SIDES ** num_dice

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Sum", "Total Outcomes", "Probability (%)"])
        for s, prob in dist.items():
            writer.writerow([s, total, f"{prob * 100:.4f}"])

    print(f"Saved to '{filename}'")


def main():
    try:
        while True:
            print("\n--Welcome to Dice Roll Probability Calculator")
            print("\n1. Sum Probability")
            print("2. At Least k Successes")
            print("3. At Most k Successes")
            print("4. Export All Sums to CSV")
            print("0. Exit")

            try:
                choice = input("Select option: ")
            except (EOFError, KeyboardInterrupt):
                print("\nGoodbye!")
                break

            if   choice == "1": sum_probability()
            elif choice == "2": at_least_success_interactive()
            elif choice == "3": at_most_success_interactive()
            elif choice == "4": all_possible_sums()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid option.")
    except Exception as error:
        print(f"Unexpected error: {error}")
    finally:
        sys.exit(0)
        
if __name__ == "__main__":
    main()            
