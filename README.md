# 🎲 Dice Roll Probability Calculator

A command-line Python tool for calculating the probability of outcomes when rolling standard six-sided dice. Whether you're analyzing tabletop game odds, studying probability theory, or just curious about your chances at the gaming table, this tool gives you precise answers fast.

---

## Features

- **Sum Probability** — Find the probability of rolling a specific total in one throw, and the cumulative probability of hitting that total at least once across multiple throws.
- **At Least k Successes** — Calculate the probability of achieving a target sum on at least *k* throws out of a given number of attempts.
- **At Most k Successes** — Calculate the probability of achieving a target sum on no more than *k* throws out of a given number of attempts.
- **Export All Sums to CSV** — Generate a full distribution table of all possible sums and their probabilities, saved as a CSV file for further analysis.

---

## Requirements

- Python 3.7 or higher
- No external dependencies — uses only the Python standard library (`csv`, `math`)

---

## Usage

Run the script and you will be greeted by an interactive menu:

```
--Welcome to Dice Roll Probability Calculator

1. Sum Probability
2. At Least k Successes
3. At Most k Successes
4. Export All Sums to CSV
0. Exit
```

### Option 1 — Sum Probability

Enter the number of dice, the number of throws, and your target sum. The calculator returns:
- The probability of rolling that exact sum on a single throw
- The probability of rolling that sum **at least once** across all throws

**Example:**
> 2 dice, 5 throws, target sum of 7 → ~16.67% per throw, ~58.56% at least once

---

### Option 2 — At Least k Successes

Define a "success" as rolling a sum greater than or equal to a threshold. Enter the number of dice, number of throws, threshold value, and minimum number of successes required. The calculator uses the binomial distribution to return the probability of hitting at least *k* successes.

**Example:**
> 2 dice, 10 throws, threshold ≥ 10, at least 3 successes → exact probability shown

---

### Option 3 — At Most k Successes

Same as above, but returns the probability of achieving **at most** *k* successes — useful for calculating the chance of a low-roll streak or conservative outcomes.

---

### Option 4 — Export All Sums to CSV

Provide the number of dice and throws, then optionally name your output file (defaults to `sums.csv`). The exported file includes three columns:

| Sum | Total Outcomes | Probability (%) |
|-----|----------------|-----------------|
| 2   | 36             | 2.7778          |
| 7   | 36             | 16.6667         |
| 12  | 36             | 2.7778          |

---

## How It Works

The calculator builds an exact probability distribution for all possible sums by iteratively convolving the outcomes of each die. For multi-throw calculations, it applies the **binomial probability formula** to model independent repeated trials — giving you accurate results without relying on simulation or approximation.

---

## Configuration

By default, the calculator uses standard **6-sided dice**. To change to a different die type, update the constant at the top of the script:

```python
SIDES = 6  # Change to 4, 8, 10, 12, or 20 for other die types
```

---
