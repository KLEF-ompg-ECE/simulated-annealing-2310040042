import random
import math
import matplotlib.pyplot as plt

# Exam data
exams = {
    "Mathematics": [1, 2, 3],
    "Physics": [1, 4, 5],
    "Chemistry": [2, 3, 4],
    "Biology": [1, 5, 6],
    "English": [2, 6, 7],
    "Computer Science": [3, 4, 7],
    "Economics": [5, 6, 8],
    "Statistics": [1, 2, 8],
    "History": [4, 7, 8],
    "Geography": [3, 5, 8]
}

num_slots = 5

def count_clashes(timetable):
    """Count total exam clashes (students with 2 exams in same slot)."""
    clashes = 0
    for student in range(1, 9):
        exams_in_slot = {}
        for exam, students in exams.items():
            if student in students:
                slot = timetable[exam]
                exams_in_slot[slot] = exams_in_slot.get(slot, 0) + 1
        for count in exams_in_slot.values():
            if count > 1:
                clashes += count - 1
    return clashes

def generate_neighbor(timetable):
    """Generate neighbor by moving one exam to a different slot."""
    neighbor = timetable.copy()
    exam = random.choice(list(neighbor.keys()))
    new_slot = random.randint(1, num_slots)
    neighbor[exam] = new_slot
    return neighbor

def run_sa(initial_temp=100.0, cooling_rate=0.995, min_temp=0.1, max_iterations=5000, seed=None):
    """Run Simulated Annealing algorithm."""
    if seed is not None:
        random.seed(seed)
    
    # Initialize random timetable
    current = {exam: random.randint(1, num_slots) for exam in exams}
    best = current.copy()
    
    current_clashes = count_clashes(current)
    best_clashes = current_clashes
    
    T = initial_temp
    iteration = 0
    clashes_history = [current_clashes]
    temp_history = [T]
    
    while T > min_temp and iteration < max_iterations:
        neighbor = generate_neighbor(current)
        neighbor_clashes = count_clashes(neighbor)
        delta = neighbor_clashes - current_clashes
        
        # Acceptance criterion
        if delta < 0 or random.random() < math.exp(-delta / T):
            current = neighbor
            current_clashes = neighbor_clashes
        
        # Track best solution
        if current_clashes < best_clashes:
            best = current.copy()
            best_clashes = current_clashes
        
        clashes_history.append(best_clashes)
        temp_history.append(T)
        
        # Cool down
        T *= cooling_rate
        iteration += 1
    
    return best, best_clashes, clashes_history, temp_history

def print_timetable(timetable):
    """Print timetable in readable format."""
    print("  Final Timetable")
    print("------------------------------------------")
    for slot in range(1, num_slots + 1):
        slot_exams = [exam for exam, s in timetable.items() if s == slot]
        print(f"  Slot {slot}:  {', '.join(slot_exams)}")
    print("------------------------------------------")

def save_plot(clashes_history, temp_history, filepath, title):
    """Save convergence plot."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    ax1.plot(clashes_history, 'b-', linewidth=1.5)
    ax1.set_xlabel('Iteration')
    ax1.set_ylabel('Best Clashes')
    ax1.set_title(f'{title} - Best Clashes Over Time')
    ax1.grid(True, alpha=0.3)
    
    ax2.plot(temp_history, 'r-', linewidth=1.5)
    ax2.set_xlabel('Iteration')
    ax2.set_ylabel('Temperature')
    ax2.set_title('Temperature Schedule')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(filepath, dpi=100)
    plt.close()
    print(f"  Plot saved to {filepath}")

if __name__ == "__main__":
    import os
    os.makedirs("plots", exist_ok=True)
    
    # --- EXPERIMENT 1 (baseline) ---
    print("=" * 50)
    print("EXPERIMENT 1 — Baseline (cooling_rate=0.995)")
    print("=" * 50)
    tt1, clashes1, cl1, tl1 = run_sa(
        initial_temp=100.0, cooling_rate=0.995,
        min_temp=0.1, max_iterations=5000, seed=42
    )
    print_timetable(tt1)
    print(f"  Final clashes: {clashes1}")
    save_plot(cl1, tl1, "plots/experiment_1.png", "Experiment 1 - Baseline")
    
    # --- EXPERIMENT 2 (cooling rate comparison) ---
    print("\n" + "=" * 50)
    print("EXPERIMENT 2 — Cooling Rate Comparison")
    print("=" * 50)
    
    # Experiment 2a - cooling_rate = 0.80
    print("\n--- Experiment 2a: cooling_rate=0.80 ---")
    tt2a, clashes2a, cl2a, tl2a = run_sa(
        initial_temp=100.0, cooling_rate=0.80,
        min_temp=0.1, max_iterations=5000, seed=42
    )
    print_timetable(tt2a)
    print(f"  Final clashes: {clashes2a}")
    save_plot(cl2a, tl2a, "plots/experiment_2a.png", "Experiment 2a - cooling_rate=0.80")
    
    # Experiment 2b - cooling_rate = 0.95
    print("\n--- Experiment 2b: cooling_rate=0.95 ---")
    tt2b, clashes2b, cl2b, tl2b = run_sa(
        initial_temp=100.0, cooling_rate=0.95,
        min_temp=0.1, max_iterations=5000, seed=42
    )
    print_timetable(tt2b)
    print(f"  Final clashes: {clashes2b}")
    save_plot(cl2b, tl2b, "plots/experiment_2b.png", "Experiment 2b - cooling_rate=0.95")
    
    # Experiment 2c - cooling_rate = 0.995
    print("\n--- Experiment 2c: cooling_rate=0.995 ---")
    tt2c, clashes2c, cl2c, tl2c = run_sa(
        initial_temp=100.0, cooling_rate=0.995,
        min_temp=0.1, max_iterations=5000, seed=42
    )
    print_timetable(tt2c)
    print(f"  Final clashes: {clashes2c}")
    save_plot(cl2c, tl2c, "plots/experiment_2c.png", "Experiment 2c - cooling_rate=0.995")
    
    # Summary
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"Experiment 1 (0.995): {clashes1} clashes")
    print(f"Experiment 2a (0.80): {clashes2a} clashes")
    print(f"Experiment 2b (0.95): {clashes2b} clashes")
    print(f"Experiment 2c (0.995): {clashes2c} clashes")
    print("\nAll plots saved to plots/ folder.")