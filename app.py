from flask import Flask, render_template, request
import time
from itertools import combinations

app = Flask(__name__)

menus = {
    "breakfast": [
        {"name": "Poha",        "price": 20, "value": 30, "nutrition": 40, "category": "Main"},
        {"name": "Upma",        "price": 25, "value": 35, "nutrition": 45, "category": "Main"},
        {"name": "Idli",        "price": 15, "value": 25, "nutrition": 35, "category": "Main"},
        {"name": "Dosa",        "price": 20, "value": 35, "nutrition": 40, "category": "Main"},
        {"name": "Sandwich",    "price": 25, "value": 40, "nutrition": 50, "category": "Main"},
        {"name": "BreadButter", "price": 15, "value": 20, "nutrition": 25, "category": "Main"},
        {"name": "Toast",       "price": 20, "value": 25, "nutrition": 30, "category": "Main"},
        {"name": "Omelette",    "price": 30, "value": 45, "nutrition": 70, "category": "Protein"},
        {"name": "BoiledEgg",   "price": 10, "value": 20, "nutrition": 60, "category": "Protein"},
        {"name": "Tea",         "price": 10, "value": 15, "nutrition": 10, "category": "Beverage"},
        {"name": "Coffee",      "price": 15, "value": 20, "nutrition": 10, "category": "Beverage"},
        {"name": "Milk",        "price": 20, "value": 25, "nutrition": 50, "category": "Beverage"},
        {"name": "Cornflakes",  "price": 30, "value": 35, "nutrition": 40, "category": "Main"},
        {"name": "Banana",      "price": 10, "value": 15, "nutrition": 30, "category": "Fruit"},
        {"name": "Apple",       "price": 20, "value": 30, "nutrition": 35, "category": "Fruit"},
        {"name": "Juice",       "price": 20, "value": 30, "nutrition": 25, "category": "Beverage"},
        {"name": "Cutlet",      "price": 25, "value": 35, "nutrition": 40, "category": "Snack"},
        {"name": "Samosa",      "price": 15, "value": 25, "nutrition": 20, "category": "Snack"},
        {"name": "VadaPav",     "price": 20, "value": 30, "nutrition": 35, "category": "Snack"},
        {"name": "Biscuit",     "price": 10, "value": 15, "nutrition": 10, "category": "Snack"},
    ],
    "lunch": [
        {"name": "Rice",           "price": 20, "value": 30, "nutrition": 40, "category": "Main"},
        {"name": "Dal",            "price": 25, "value": 35, "nutrition": 55, "category": "Protein"},
        {"name": "Chapati",        "price": 10, "value": 15, "nutrition": 25, "category": "Main"},
        {"name": "Paneer",         "price": 55, "value": 75, "nutrition": 80, "category": "Protein"},
        {"name": "Biryani",        "price": 60, "value": 80, "nutrition": 70, "category": "Main"},
        {"name": "MixedVeg",       "price": 40, "value": 50, "nutrition": 65, "category": "Vegetable"},
        {"name": "PalakPaneer",    "price": 50, "value": 70, "nutrition": 85, "category": "Protein"},
        {"name": "Rajma",          "price": 35, "value": 50, "nutrition": 70, "category": "Protein"},
        {"name": "Chole",          "price": 35, "value": 50, "nutrition": 65, "category": "Protein"},
        {"name": "Curd",           "price": 20, "value": 25, "nutrition": 40, "category": "Dairy"},
        {"name": "Salad",          "price": 15, "value": 20, "nutrition": 30, "category": "Vegetable"},
        {"name": "Roti",           "price": 10, "value": 15, "nutrition": 25, "category": "Main"},
        {"name": "VegetableSoup",  "price": 30, "value": 40, "nutrition": 35, "category": "Soup"},
        {"name": "Khichdi",        "price": 30, "value": 45, "nutrition": 55, "category": "Main"},
        {"name": "DalTadka",       "price": 35, "value": 50, "nutrition": 60, "category": "Protein"},
        {"name": "JeeraRice",      "price": 30, "value": 40, "nutrition": 40, "category": "Main"},
        {"name": "VegPulao",       "price": 40, "value": 55, "nutrition": 50, "category": "Main"},
        {"name": "Buttermilk",     "price": 15, "value": 20, "nutrition": 30, "category": "Dairy"},
        {"name": "FruitBowl",      "price": 25, "value": 35, "nutrition": 45, "category": "Fruit"},
        {"name": "Sprouts",        "price": 20, "value": 30, "nutrition": 60, "category": "Protein"},
    ],
    "dinner": [
        {"name": "Chapati",          "price": 10, "value": 15, "nutrition": 25, "category": "Main"},
        {"name": "Dal",              "price": 25, "value": 35, "nutrition": 55, "category": "Protein"},
        {"name": "Rice",             "price": 20, "value": 30, "nutrition": 40, "category": "Main"},
        {"name": "Paneer",           "price": 55, "value": 75, "nutrition": 80, "category": "Protein"},
        {"name": "VegetableCurry",   "price": 40, "value": 50, "nutrition": 60, "category": "Vegetable"},
        {"name": "Soup",             "price": 30, "value": 40, "nutrition": 35, "category": "Soup"},
        {"name": "Salad",            "price": 15, "value": 20, "nutrition": 30, "category": "Vegetable"},
        {"name": "Curd",             "price": 20, "value": 25, "nutrition": 40, "category": "Dairy"},
        {"name": "Khichdi",          "price": 30, "value": 45, "nutrition": 55, "category": "Main"},
        {"name": "BoiledVegetables", "price": 25, "value": 35, "nutrition": 50, "category": "Vegetable"},
        {"name": "Roti",             "price": 10, "value": 15, "nutrition": 25, "category": "Main"},
        {"name": "Palak",            "price": 30, "value": 45, "nutrition": 70, "category": "Vegetable"},
        {"name": "DalFry",           "price": 35, "value": 50, "nutrition": 60, "category": "Protein"},
        {"name": "VegetableStew",    "price": 40, "value": 55, "nutrition": 65, "category": "Vegetable"},
        {"name": "GrilledPaneer",    "price": 60, "value": 80, "nutrition": 85, "category": "Protein"},
        {"name": "FruitSalad",       "price": 25, "value": 35, "nutrition": 40, "category": "Fruit"},
        {"name": "Buttermilk",       "price": 15, "value": 20, "nutrition": 30, "category": "Dairy"},
        {"name": "Sprouts",          "price": 20, "value": 30, "nutrition": 60, "category": "Protein"},
        {"name": "Oats",             "price": 25, "value": 35, "nutrition": 55, "category": "Main"},
        {"name": "Milk",             "price": 20, "value": 25, "nutrition": 50, "category": "Dairy"},
    ]
}

# ─── ALGORITHMS ───────────────────────────────────────────────────────────────

def greedy_knapsack(items, budget):
    start = time.perf_counter()
    sorted_items = sorted(items, key=lambda x: x['value'] / x['price'], reverse=True)
    total_cost, total_value, result = 0, 0, []
    for item in sorted_items:
        if total_cost + item['price'] <= budget:
            result.append(item)
            total_cost  += item['price']
            total_value += item['value']
    elapsed = round((time.perf_counter() - start) * 1000, 4)
    return result, total_cost, total_value, elapsed


def greedy_with_trace(items, budget):
    sorted_items = sorted(items, key=lambda x: x['value'] / x['price'], reverse=True)
    total_cost, total_value = 0, 0
    trace = []
    for item in sorted_items:
        ratio = round(item['value'] / item['price'], 2)
        if total_cost + item['price'] <= budget:
            action = "Selected"
            total_cost  += item['price']
            total_value += item['value']
        else:
            action = "Skipped"
        trace.append({
            "item":             item['name'],
            "price":            item['price'],
            "value":            item['value'],
            "ratio":            ratio,
            "action":           action,
            "budget_remaining": budget - total_cost,
        })
    return trace, total_cost, total_value


def dp_knapsack(items, budget):
    start = time.perf_counter()
    n  = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        p = items[i-1]['price']
        v = items[i-1]['value']
        for w in range(budget + 1):
            dp[i][w] = dp[i-1][w]
            if p <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - p] + v)
    # Traceback
    result, w = [], budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            result.append(items[i-1])
            w -= items[i-1]['price']
    total_cost  = sum(x['price'] for x in result)
    total_value = dp[n][budget]
    elapsed = round((time.perf_counter() - start) * 1000, 4)
    return result, total_cost, total_value, elapsed


def brute_force_knapsack(items, budget):
    start = time.perf_counter()
    best_value, best_combo = 0, []
    for r in range(len(items) + 1):
        for combo in combinations(items, r):
            cost = sum(x['price'] for x in combo)
            val  = sum(x['value'] for x in combo)
            if cost <= budget and val > best_value:
                best_value = val
                best_combo = list(combo)
    total_cost = sum(x['price'] for x in best_combo)
    elapsed = round((time.perf_counter() - start) * 1000, 4)
    return best_combo, total_cost, best_value, elapsed


def sensitivity_analysis(items, budget_max, steps=10):
    step = max(10, budget_max // steps)
    budgets, values, costs = [], [], []
    for b in range(step, budget_max + step, step):
        _, cost, val, _ = dp_knapsack(items, b)
        budgets.append(b)
        values.append(val)
        costs.append(cost)
    return budgets, values, costs


def complexity_data(items, budget=200):
    labels, greedy_t, dp_t, brute_t = [], [], [], []
    for n in range(2, min(len(items), 15) + 1):
        subset = items[:n]
        labels.append(n)
        _, _, _, gt = greedy_knapsack(subset, budget)
        _, _, _, dt = dp_knapsack(subset, budget)
        greedy_t.append(gt)
        dp_t.append(dt)
        if n <= 12:
            _, _, _, bt = brute_force_knapsack(subset, budget)
            brute_t.append(bt)
        else:
            brute_t.append(None)
    return labels, greedy_t, dp_t, brute_t


# ─── ROUTES ───────────────────────────────────────────────────────────────────

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/menu/<meal>', methods=['GET', 'POST'])
def menu(meal):
    items = menus.get(meal, [])
    if request.method == 'POST':
        budget   = int(request.form['budget'])
        selected = request.form.getlist('food')
        foods = []
        for f in selected:
            parts = f.split('|')
            foods.append({
                "name":      parts[0],
                "price":     int(parts[1]),
                "value":     int(parts[2]),
                "nutrition": int(parts[3]),
                "category":  parts[4],
            })
        result, total_cost, total_value, _ = greedy_knapsack(foods, budget)
        trace, _, _ = greedy_with_trace(foods, budget)
        nutrition = sum(x['nutrition'] for x in result)
        return render_template('result.html',
            result=result, total=total_cost, value=total_value,
            nutrition=nutrition, meal=meal, trace=trace)
    return render_template('menu.html', items=items, meal=meal)


@app.route('/compare/<meal>', methods=['GET', 'POST'])
def compare(meal):
    items = menus.get(meal, [])
    if request.method == 'POST':
        budget   = int(request.form['budget'])
        selected = request.form.getlist('food')
        foods = []
        for f in selected:
            parts = f.split('|')
            foods.append({
                "name":      parts[0],
                "price":     int(parts[1]),
                "value":     int(parts[2]),
                "nutrition": int(parts[3]),
                "category":  parts[4],
            })
        g_res, g_cost, g_val, g_time = greedy_knapsack(foods, budget)
        d_res, d_cost, d_val, d_time = dp_knapsack(foods, budget)
        b_res, b_cost, b_val, b_time = brute_force_knapsack(foods, budget) if len(foods) <= 15 else ([], 0, 0, 0)
        trace, _, _ = greedy_with_trace(foods, budget)

        # Sensitivity
        s_budgets, s_values, s_costs = sensitivity_analysis(foods, budget + 100)

        # Complexity
        cl, cg, cd, cb = complexity_data(foods, budget)

        import json
        return render_template('compare.html',
            meal=meal, budget=budget,
            greedy={"selected": g_res, "cost": g_cost, "value": g_val, "time": g_time},
            dp    ={"selected": d_res, "cost": d_cost, "value": d_val, "time": d_time},
            brute ={"selected": b_res, "cost": b_cost, "value": b_val, "time": b_time},
            trace=trace,
            s_budgets=s_budgets, s_values=s_values, s_costs=s_costs,
            cl=cl, cg=cg, cd=cd, cb=cb,
            cl_max=len(cl) + 1,
            # Pre-serialized JSON strings — avoids all Jinja-in-JS issues
            j_cl=json.dumps(cl),
            j_cg=json.dumps(cg),
            j_cd=json.dumps(cd),
            j_cb=json.dumps(cb),
            j_s_budgets=json.dumps(s_budgets),
            j_s_values=json.dumps(s_values),
            j_s_costs=json.dumps(s_costs),
            too_large=(len(foods) > 15),
        )
    return render_template('menu.html', items=items, meal=meal, compare_mode=True)


if __name__ == "__main__":
    app.run(debug=True)