# Define the employee data dictionary
emp = {
    'ename': ['hari', 'thomas', 'raj', 'laksh', 'subha'],
    'age': [21, 23, 22, 35, 20],
    'salary': [20000, 35000, 22000, 41000, 30000]
}

# Print the entire employee data
print("The employee data is:", emp)

# Print the employee salaries using dictionary access
print("The employee salaries are:")
print(emp['salary'])  # Correct access to the 'salary' key

# Print each salary on a new line
print("The salaries are:")
for v in emp['salary']:
    print(v)

# Get the list of salaries
l1 = emp['salary']

# Print the list of salaries
print("The listed salaries:", l1)

# Print the sorted list of salaries
print('The stored salaries are:', sorted(l1))



"navyaa marri"