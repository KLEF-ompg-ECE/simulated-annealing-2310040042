# Assignment 1 — Simulated Annealing: Exam Timetable Scheduling
## Observation Report

Student Name  : Harsha  
Student ID    : 2310040042  
Date Submitted: March 26, 2026  

---

## How to Submit

1. Run each experiment following the instructions below
2. Fill in every answer box — do not leave placeholders
3. Make sure the plots/ folder contains all required images
4. Commit this README and the plots/ folder to your GitHub repo

---

## Before You Begin — Read the Code

Open sa_timetable.py and read through it. Then answer these questions.

Q1. What does `count_clashes()` measure? What value means a perfect timetable?

count_clashes() measures the total number of clashes across all students, where a clash occurs when a student has two or more exams assigned to the same time slot. The function iterates through each student's exam schedule and counts how many times a student is double-booked. A value of 0 means a perfect timetable with no scheduling conflicts.

Q2. What does `generate_neighbor()` do? How is the new timetable different from the current one?

generate_neighbor() creates a neighboring solution by randomly selecting one exam and reassigning it to a different time slot. The new timetable differs from the current one in exactly one position - one exam's slot assignment is changed while all other exams remain in their original slots. This small perturbation allows the algorithm to explore nearby solutions in the search space.

Q3. In `run_sa()`, there is this line:
if delta < 0 or random.random() < math.exp(-delta / T):
What does this line decide? Why does SA sometimes accept a worse solution?

This line decides whether to accept the neighboring solution. It always accepts improvements (delta < 0) but also sometimes accepts worse solutions based on a probability that depends on the temperature T. At high temperatures, worse solutions have a higher acceptance probability, allowing the algorithm to escape local minima. As temperature decreases, the algorithm becomes more selective, focusing on better solutions. This trade-off between exploration and exploitation is what makes Simulated Annealing effective.

---

## Experiment 1 — Baseline Run

Instructions: Run the program without changing anything.
python sa_timetable.py

Fill in this table:

| Metric | Your result |
|--------|-------------|
| Number of iterations completed | 1379 |
| Clashes at iteration 1 | 12 |
| Final best clashes | 3 |
| Did SA reach 0 clashes? (Yes / No) | No |

Copy the printed timetable output here:
Final Timetable
------------------------------------------
  Slot 1:  Geography
  Slot 2:  Chemistry, English
  Slot 3:  History, Computer Science, Economics
  Slot 4:  Biology, Statistics
  Slot 5:  Mathematics, Physics
------------------------------------------
  Total clashes: 3

Look at `plots/experiment_1.png` and describe what you see (2–3 sentences).  
*Where does the biggest drop in clashes happen? Does the curve flatten out?*
The clash plot shows a steep decline in the first 200-300 iterations where clashes drop from 12 to around 5-6, representing the initial exploration phase. After this rapid improvement, the curve gradually flattens with minor oscillations, indicating that the algorithm is making smaller improvements as it converges. The temperature plot shows a logarithmic decay pattern, gradually cooling over the 1379 iterations.

---

## Experiment 2 — Effect of Cooling Rate

Instructions: In sa_timetable.py, find the # EXPERIMENT 2 block in __main__.  
Copy it three times and run with cooling_rate = 0.80, 0.95, and 0.995.  
Save plots as experiment_2a.png, experiment_2b.png, experiment_2c.png.

Results table:

| cooling_rate | Final clashes | Iterations completed | Reached 0 clashes? |
|-------------|---------------|----------------------|--------------------|
| 0.80        | 8             | 31                   | No                 |
| 0.95        | 3             | 135                  | No                 |
| 0.995       | 3             | 1379                 | No                 |
Compare the three plots. What do you notice about how fast vs slow cooling affects the result? (3–4 sentences)  
*Hint: Fast cooling = temperature drops quickly. Does it have time to explore well?*
Fast cooling (0.80) terminates quickly after only 31 iterations with a poor result of 8 clashes, indicating the algorithm converged prematurely without sufficient exploration. Medium cooling (0.95) reaches a good solution (3 clashes) in 135 iterations, achieving a balance between exploration and exploitation. Slow cooling (0.995) takes significantly longer (1379 iterations) but achieves the same final result (3 clashes) as medium cooling. This demonstrates that slower cooling allows more thorough exploration, but beyond a certain point, the improvement plateaus while only increasing computation time.

Which cooling_rate gave the best result? Why do you think that is?
Both 0.95 and 0.995 gave the same best result of 3 clashes, but 0.95 achieved this in much less time (135 vs 1379 iterations). The 0.95 cooling rate provides better computational efficiency because it maintains enough temperature for exploration while still progressing toward exploitation. Even slower cooling (0.995) doesn't improve the solution further, suggesting that 0.95 is in the practical sweet spot where the algorithm balances thorough search with reasonable computation time.

---

## Summary

Complete this table with your best result from each experiment:

| Experiment | Key setting | Final clashes | Main finding in one sentence |
|------------|-------------|---------------|------------------------------|
| 1 — Baseline | cooling_rate = 0.995 | 3 | Slow cooling provides thorough exploration but requires more computation to achieve the same solution quality as medium cooling rates. |
| 2 — Cooling rate | cooling_rate = 0.95 | 3 | Medium cooling rate (0.95) achieves optimal results with significantly faster convergence and better computational efficiency than both faster and slower rates. |

In your own words — what is the most important thing you learned about Simulated Annealing from these experiments? (3–5 sentences)
The most important lesson is that Simulated Annealing is fundamentally about balance. The cooling rate parameter controls this balance between exploration (searching broadly for good solutions) and exploitation (refining found solutions). A cooling rate that is too fast (0.80) doesn't allow time for exploration and gets stuck in poor local minima. Conversely, an extremely slow cooling rate (0.995) explores thoroughly but wastes computation achieving the same result as a more moderate rate (0.95). The key insight is that there exists an optimal "sweet spot" where you balance these two competing objectives—for this problem, that appears to be around 0.95, where the algorithm reaches good solutions efficiently.

---

## Submission Checklist

- [x] Student name and ID filled in
- [x] Q1, Q2, Q3 answered
- [x] Experiment 1: table filled, timetable pasted, plot observation written
- [x] Experiment 2: results table filled (3 rows), observation and answer written
- [x] Summary table completed and reflection written
- [x] plots/ contains: experiment_1.png, experiment_2a.png, experiment_2b.png, experiment_2c.png