# 📌 CODTECH Task-4: Product Mix Optimization (with Interactive Inputs & Detailed Comments)

# ✅ STEP 1: Install the PuLP library (only needed the first time)
# PuLP is a Python library used for solving linear programming problems.
!pip install pulp

# ✅ STEP 2: Import the PuLP library
import pulp

# ✅ STEP 3: Take user inputs
# Ask user to enter the values for profits, labor, and material requirements

# 🔢 Profit earned per unit of each product
profit_a = float(input("Enter profit per unit of Product A (₹): "))
profit_b = float(input("Enter profit per unit of Product B (₹): "))

# 🧠 Labor needed for each product and total labor available
labor_a = float(input("Enter labor hours required for Product A: "))
labor_b = float(input("Enter labor hours required for Product B: "))
total_labor = float(input("Enter total available labor hours: "))

# 🧱 Material needed for each product and total material available
material_a = float(input("Enter material units required for Product A: "))
material_b = float(input("Enter material units required for Product B: "))
total_material = float(input("Enter total available material units: "))

# ✅ STEP 4: Create the optimization problem
# We are maximizing profit, so use LpMaximize
problem = pulp.LpProblem("Product_Mix_Optimization", pulp.LpMaximize)

# ✅ STEP 5: Define the decision variables (x and y must be >= 0)
x = pulp.LpVariable('Product_A', lowBound=0, cat='Continuous')  # units of A
y = pulp.LpVariable('Product_B', lowBound=0, cat='Continuous')  # units of B

# ✅ STEP 6: Define the objective function (maximize total profit)
problem += profit_a * x + profit_b * y, "Total_Profit"

# ✅ STEP 7: Add constraints
# Constraint 1: Total labor used must be ≤ available labor
problem += labor_a * x + labor_b * y <= total_labor, "Labor_Constraint"

# Constraint 2: Total material used must be ≤ available material
problem += material_a * x + material_b * y <= total_material, "Material_Constraint"

# ✅ STEP 8: Solve the problem using PuLP's built-in solver
problem.solve()

# ✅ STEP 9: Print the results
print("\n📊 Solution Status:", pulp.LpStatus[problem.status])

# Print how many units of each product to make
print("✅ Optimal Production Plan:")
print(f" - Product A Units: {x.varValue}")
print(f" - Product B Units: {y.varValue}")

# Print the maximum profit
print("💰 Maximum Profit (₹):", pulp.value(problem.objective))
