!pip install pulp 
# STEP 1: Import the PuLP library
import pulp

# STEP 2: Take user inputs
profit_a = float(input("Enter profit per unit of Product A: "))
profit_b = float(input("Enter profit per unit of Product B: "))

labor_a = float(input("Enter labor hours required for Product A: "))
labor_b = float(input("Enter labor hours required for Product B: "))
total_labor = float(input("Enter total available labor hours: "))

material_a = float(input("Enter material units required for Product A: "))
material_b = float(input("Enter material units required for Product B: "))
total_material = float(input("Enter total available material units: "))

# STEP 3: Create the optimization problem
problem = pulp.LpProblem("Product_Mix_Optimization", pulp.LpMaximize)

# STEP 4: Define the decision variables
x = pulp.LpVariable('Product_A', lowBound=0, cat='Continuous')
y = pulp.LpVariable('Product_B', lowBound=0, cat='Continuous')

# STEP 5: Objective function
problem += profit_a * x + profit_b * y, "Total_Profit"

# STEP 6: Constraints
problem += labor_a * x + labor_b * y <= total_labor, "Labor_Constraint"
problem += material_a * x + material_b * y <= total_material, "Material_Constraint"

# STEP 7 : Solve the problem
problem.solve()

# STEP 8: Output
print("\nSolution Status:", pulp.LpStatus[problem.status])
print("Optimal Production Plan:")
print(f" - Product A Units: {x.varValue}")
print(f" - Product B Units: {y.varValue}")
print("Maximum Profit (in rupees):", pulp.value(problem.objective))
