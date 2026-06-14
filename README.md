# 🎲 Dice Roll Probability Calculator

A command-line tool for calculating probabilities of dice roll outcomes using combinatorics and binomial distribution.

---
## Youtube video of Project 

link : https://youtu.be/rrUFaeUkHLY

---
## Features

- Calculate the probability of a specific sum from rolling multiple dice
- Find the probability of achieving **at least k successes** across multiple throws
- Find the probability of achieving **at most k successes** across multiple throws
- Export a full sum probability distribution to a **CSV file**

---

## Requirements

- Python 3.x (no external libraries required — uses only `csv` and `math` from the standard library)

---

## Usage

Run the script from your terminal:

```bash
python main.py
```

You will see the main menu:

```
--Welcome to Dice Roll Probability Calculator

1. Sum Probability
2. At Least k Successes
3. At Most k Successes
4. Export All Sums to CSV
0. Exit
```

---

## Menu Options

### 1. Sum Probability

Calculates the probability that a given number of dice rolled simultaneously will produce a specific sum.

**Example:**
```
Enter number of dice thrown at once: 2
Enter target sum (2 to 12): 7
Probability: 6/36 or 16.6667%
```

---

### 2. At Least k Successes

Uses the **binomial distribution** to calculate the probability of getting a target sum **at least k times** over multiple throws.

**Inputs:**
- Number of dice per throw
- Number of throws
- Target sum (defines what counts as a "success")
- Minimum number of successes (k)

**Example:**
```
Enter number of dice: 2
Enter number of throws: 10
Enter success value (sum = ?, range 2-12): 7
Enter minimum number of successes: 3
Probability of at least 3 success(es): 55.0934%
```

---

### 3. At Most k Successes

Calculates the probability of getting the target sum **at most k times** over multiple throws.

**Inputs:** Same as option 2, but asks for a **maximum** number of successes.

**Example:**
```
Enter number of dice: 2
Enter number of throws: 10
Enter success value (sum = ?, range 2-12): 7
Enter maximum number of successes: 2
Probability of at most 2 success(es): 44.9066%
```

---

### 4. Export All Sums to CSV

Generates a CSV file containing every possible sum for a given number of dice, along with the total sample space size and probability percentage.

**Example output (`sums.csv`):**

| Sum | Sample Space | Probability (%) |
|-----|-------------|-----------------|
| 2   | 36          | 2.7778          |
| 3   | 36          | 5.5556          |
| 7   | 36          | 16.6667         |
| 12  | 36          | 2.7778          |

---

## How It Works

### Sum Distribution (`get_sum_distribution`)

Iteratively convolves dice face values to build a frequency map of all possible sums. For `n` dice with 6 sides, the total sample space is `6ⁿ`.

### Binomial Probability

Options 2 and 3 use the **binomial formula**:

```
P(X = k) = C(n, k) * p^k * (1-p)^(n-k)
```

Where:
- `n` = number of throws
- `k` = number of successes
- `p` = probability of the target sum on a single throw

---

## Project Structure

```
.
root/
    ├── project.py       # Main script with all logic
    ├── test_project.py  # Testing of the main script
```

---

## Notes

- The calculator assumes **standard fair 6-sided dice**.
- The number of dice and throw counts can be any positive integer, but very large values may slow down the distribution calculation.
- CSV files are saved in the current working directory unless a full path is specified.
