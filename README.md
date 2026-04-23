# 🍽️ Mess Food Optimizer

A web app that helps students choose the best mess food within their budget using classic DAA algorithms.

## Algorithms Used
- **Greedy** — O(n log n), sorts by value/price ratio
- **Dynamic Programming** — O(n×W), always optimal 0/1 Knapsack
- **Brute Force** — O(2ⁿ), exhaustive subset search

## Features
- Algorithm comparison with live charts
- Step-by-step greedy trace table
- Budget sensitivity analysis
- Time complexity growth visualization
- Breakfast, Lunch & Dinner menus

## How to Run
```bash
pip install flask
python app.py
```
Then open http://127.0.0.1:5000 in your browser.

## Tech Stack
- Python + Flask
- Jinja2 Templates
- Chart.js
- HTML/CSS