# 🧠 Rubik's Cube Solver using CSP (Constraint Satisfaction Problem)

A Python-based Rubik’s Cube solver that applies **Artificial Intelligence** techniques like **Backtracking** and **Forward Checking** to find valid cube states using **Constraint Satisfaction Problem (CSP)** modeling.

> 🎯 Focused on classical AI problem-solving—not standard Rubik’s Cube algorithms!

---

## 🚀 Features

- ✅ CSP modeling of the Rubik’s Cube
- 🔁 Backtracking search for solution exploration
- 🔍 Forward checking for early pruning
- 🧱 Simple, single-file Python implementation

---

## 📘 What is CSP?

A **Constraint Satisfaction Problem (CSP)** is a mathematical question defined by:
- A set of variables
- A set of possible values (domains)
- A set of constraints specifying allowable combinations

### In This Project:
- **Variables** = Cube facelets
- **Domains** = `{ R, G, B, Y, O, W }` (colors)
- **Constraints** = Valid cube color configurations

---

## 🧠 How It Works

1. **Represent the Cube** in a simplified data structure
2. **Apply Backtracking** to explore possible color assignments
3. **Use Forward Checking** to eliminate invalid paths early
4. **Return a solution** that satisfies all constraints

---

## 🛠 Requirements

- Python 3.7+
- No external libraries required

---

## ▶️ Run the Project

```bash
python rubiks_cube_csp_solver.py


📁 RubiksCubeCSP/
├── rubiks_cube_csp_solver.py   # 💡 All logic and solver code in one file
├── README.md                   # 📘 You are here!
