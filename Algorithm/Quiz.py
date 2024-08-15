import numpy as np

def label():
    A = np.array([['ENG','SWE','NOR','GER','DEN'],
                  ['red','green','white','yellow','blue'],
                  ['coffee','milk','beer','water','tea'],
                  ['LEXUS','BWM','BENZ','GM','FORD'],
                  ['dog','bird','cat','horse','fish']])
    return A

def encoder(A):
    B = np.arange(5*5).reshape(5,5)
    #Dict Mapping
    categories = {}
    for i in range(5):
        for j in range(5):
            categories[A[i,j]] = B[i,j]
    return categories

A = label()
data = encoder(A)
print(data)



###############################################################################################
from ortools.sat.python import cp_model

# Define categories
categories = {'Eng': 0, 'Math': 1, 'Sci': 2}

# Define the model
model = cp_model.CpModel()

# Define variables
num_rows = 5
num_cols = 5
X = [[model.NewIntVar(0, 2, f'X_{i}_{j}') for j in range(num_cols)] for i in range(num_rows)]

# Add constraint X[1][j] = 'Eng' for all columns j
for j in range(num_cols):
    model.Add(X[1][j] == categories['Eng'])

# Add other example constraints and objective if necessary
# For example, X[2][2] should be 'Math'
model.Add(X[2][2] == categories['Math'])

# Create the solver and solve the model
solver = cp_model.CpSolver()
status = solver.Solve(model)

# Print the results
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print('Solution:')
    for i in range(num_rows):
        row = [solver.Value(X[i][j]) for j in range(num_cols)]
        print(row)
else:
    print('No solution found.')

