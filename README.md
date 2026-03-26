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
```
count_clashes() measures the total number of clashes across all students, where a clash occurs when a student has two exams in the same slot. 0 means a perfect timetable.
```

Q2. What does `generate_neighbor()` do? How is the new timetable different from the current one?
```
generate_neighbor() creates a neighbouring timetable when one randomly selected exam is rescheduled to a different slot; only one exam assignment changes.
```

Q3. In `run_sa()`, there is this line:
`if delta < 0 or random.random() < math.exp(-delta / T):`
What does this line decide? Why does SA sometimes accept a worse solution?
```
This line decides whether to accept the neighbor solution: always accept if it improves (delta < 0), otherwise accept worse solution with probability exp(-delta/T). Worse solutions are accepted to escape local minima during high temperature.
```

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
```
Final Timetable
------------------------------------------
  Slot 1:  Geography
  Slot 2:  Chemistry, English
  Slot 3:  History, Computer Science, Economics
  Slot 4:  Biology, Statistics
  Slot 5:  Mathematics, Physics
------------------------------------------
  Total clashes: 3
```

Look at `plots/experiment_1.png` and describe what you see (2–3 sentences).  
*Where does the biggest drop in clashes happen? Does the curve flatten out?*
```
The clash plot shows a steep decline in the first 200-300 iterations, then flattens with smaller improvements. Temperature plot decays exponentially over 1379 iterations.
```


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
```
Fast cooling (0.80) converges quickly with poor quality. Medium cooling (0.95) gives good quality and efficiency. Slow cooling (0.995) achieves similar quality but needs more iterations.
```

Which cooling_rate gave the best result? Why do you think that is?
```
0.95 gave the best trade-off in this run because it found a low clash solution faster than 0.995 and better than 0.80.
```

---

## Summary

Complete this table with your best result from each experiment:

| Experiment | Key setting | Final clashes | Main finding in one sentence |
|------------|-------------|---------------|------------------------------|
| 1 — Baseline | cooling_rate = 0.995 | 3 | Slow cooling provides thorough exploration but requires more computation to achieve the same solution quality as medium cooling rates. |
| 2 — Cooling rate | cooling_rate = 0.95 | 3 | Medium cooling rate (0.95) achieves optimal results with significantly faster convergence and better computational efficiency than both faster and slower rates. |

In your own words — what is the most important thing you learned about Simulated Annealing from these experiments? (3–5 sentences)
```
The most important lesson is that Simulated Annealing needs a tuned cooling schedule. Too fast cooling may trap in local minima, and too slow cooling takes too long. A moderate rate around 0.95 gave the best efficiency in these tests.
```
---

## Submission Checklist

- [x] Student name and ID filled in
- [x] Q1, Q2, Q3 answered
- [x] Experiment 1: table filled, timetable pasted, plot observation written
- [x] Experiment 2: results table filled (3 rows), observation and answer written
- [x] Summary table completed and reflection written
- [x] plots/ contains: experiment_1.png, experiment_2a.png, experiment_2b.png, experiment_2c.png