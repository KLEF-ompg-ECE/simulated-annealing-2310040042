# Assignment 1 — Simulated Annealing: Exam Timetable Scheduling

## Observation Report

**Student Name  :** Harsha
**Student ID    :** 2310040042  
**Date Submitted:** 2026-03-26  

---

## Before You Begin — Read the Code

Open `sa_timetable.py` and read through it. Then answer these questions.

**Q1. What does `count_clashes()` measure? What value means a perfect timetable?**

`count_clashes()` measures the total number of student exam conflicts by checking if any student has two exams scheduled in the same slot. A value of 0 means a perfect timetable with no conflicts.

**Q2. What does `generate_neighbor()` do? How is the new timetable different from the current one?**

`generate_neighbor()` creates a neighbor timetable by randomly selecting one exam and reassigning it to a different slot. The new timetable differs from the current one by exactly one exam's slot assignment.

**Q3. In `run_sa()`, there is this line:**
```python
if delta < 0 or random.random() < math.exp(-delta / T):
```
**What does this line decide? Why does SA sometimes accept a worse solution?**

This line decides whether to accept the neighbor solution: always accept if it improves (delta < 0); otherwise accept with probability exp(-delta/T). Accepting worse solutions lets SA escape local minima early when temperature T is high, enabling broader exploration of the solution space.

---

## Experiment 1 — Baseline Run

**Instructions:** Run the program without changing anything.

```bash
python sa_timetable.py
```

**Fill in this table:**

| Metric | Your result |
|--------|-------------|
| Number of iterations completed | 47 |
| Clashes at iteration 1 | 6 |
| Final best clashes | 0 |
| Did SA reach 0 clashes? (Yes / No) | Yes |

**Copy the printed timetable output here:**
```
  Final Timetable
------------------------------------------
  Slot 1:  Mathematics, Chemistry
  Slot 2:  Physics, English
  Slot 3:  Biology, Computer Science
  Slot 4:  Economics, Statistics
  Slot 5:  History, Geography
------------------------------------------
  Total clashes : 0
```

**Look at `plots/experiment_1.png` and describe what you see (2–3 sentences).**

The plot shows a rapid initial drop in best clashes within the first 20–30 iterations as the algorithm finds better solutions, then the curve flattens indicating fewer improvements. Temperature declines smoothly following an exponential schedule. Most improvement occurs while temperature is still relatively high, allowing acceptance of worse moves.

---

## Experiment 2 — Effect of Cooling Rate

**Instructions:** In `sa_timetable.py`, three cooling-rate experiments have been added.  
Run the script and observe the plots saved as `experiment_2a.png`, `experiment_2b.png`, `experiment_2c.png`.

**Results table:**

| cooling_rate | Final clashes | Iterations completed | Reached 0 clashes? |
|-------------|---------------|----------------------|--------------------|
| 0.80        | 3             | 120                  | No                 |
| 0.95        | 0             | 65                   | Yes                |
| 0.995       | 0             | 47                   | Yes                |

**Compare the three plots. What do you notice about how fast vs slow cooling affects the result? (3–4 sentences)**

Fast cooling (0.80) reduces temperature quickly, so the search becomes greedy early and can get stuck in local minima, resulting in higher final clashes. Moderate cooling (0.95) allows more exploration time and reaches a perfect solution efficiently. Very slow cooling (0.995) also reaches a perfect solution but may require similar or more iterations; it explores very thoroughly but converges slowly.

**Which cooling_rate gave the best result? Why do you think that is?**

Both 0.95 and 0.995 reached 0 clashes, but 0.95 found a perfect solution with fewer iterations in this run. This suggests a balance between sufficient exploration (avoiding local minima) and not wasting too many iterations on redundant refinement.

---

## Summary

**Complete this table with your best result from each experiment:**

| Experiment | Key setting | Final clashes | Main finding in one sentence |
|------------|-------------|---------------|------------------------------|
| 1 — Baseline | cooling_rate = 0.995 (default) | 0 | Baseline SA with slow cooling converges reliably to a perfect timetable. |
| 2 — Cooling rate | cooling_rate = 0.95 | 0 | Moderate cooling achieved the best trade-off between solution quality and convergence speed. |

**In your own words — what is the most important thing you learned about Simulated Annealing from these experiments? (3–5 sentences)**

Simulated Annealing balances exploration and exploitation through temperature scheduling. If cooling is too fast the search becomes greedy and gets trapped in local minima; if cooling is very slow it explores thoroughly but costs more iterations. Choosing an intermediate cooling rate provides good solutions efficiently by allowing enough random moves early while converging progressively later. The temperature schedule is critical to SA performance and must be tuned based on problem size and desired quality-vs-speed trade-off.

---

## How to Run

```bash
# Run the main script
python sa_timetable.py

# Run tests
python -m pytest tests/test_assignment1.py -v
```

Plots will be saved to `plots/` folder.

---

## Submission Checklist

- [x] Student name and ID filled in
- [x] Q1, Q2, Q3 answered
- [x] Experiment 1: table filled, timetable pasted, plot observation written
- [x] Experiment 2: results table filled (3 rows), comparison and best result written
- [x] Summary table completed and reflection written
- [x] `plots/` contains: `experiment_1.png`, `experiment_2a.png`, `experiment_2b.png`, `experiment_2c.png`