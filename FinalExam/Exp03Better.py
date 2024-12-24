employe_data = [
    {'Name': "Employee1", 'BS' : 12000},
    {'Name': "Employee2", 'BS' : 15000},
    {'Name': "Employee3", 'BS' : 22000},
    {'Name': "Employee4", 'BS' : 36000},
    {'Name': "Employee5", 'BS' : 45000},
]

def calculate_final(data):
    final = []
    for employee in data:
        total = employee['BS'] + employee['HA'] + employee['MA'] - employee['PFD']
        final.append({employee['Name'] : total})
    return final
#         print(f"Employee: {employee['Name']} Total Salery: {}")

def calculateSalary(data):
    calculated_data = []

    for employee in data:
        # employee['BS'] = employee['BS'] 
        employee['HA'] = employee['BS']*(.2)
        employee['MA'] = employee['BS']*(.15)
        employee['PFD'] = employee['BS']*(.05)
        calculated_data.append(employee)
    return calculated_data

def updateSalary(data):
    salaries = []
    names = []
    for employee in data:
        names.append(list(employee.items())[0][0])
        salaries.append(list(employee.items())[0][1])
    salaries = [i+(i*0.05) for i in salaries]
    return zip(names,salaries)


print("(a)")
for i in calculate_final(calculateSalary(employe_data)):
    print(i)

print("(c)")
for i,j in updateSalary(calculate_final(calculateSalary(employe_data))):
    print({i:j})