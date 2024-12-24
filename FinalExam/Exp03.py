# (a)

employe_data = [
    {'Name': "Employee1", 'BS' : 12000},
    {'Name': "Employee2", 'BS' : 15000},
    {'Name': "Employee3", 'BS' : 22000},
    {'Name': "Employee4", 'BS' : 36000},
    {'Name': "Employee5", 'BS' : 45000},
]

def calculateSalary(data):
    calculated_data = []

    for employee in data:
        # employee['BS'] = employee['BS'] 
        employee['HA'] = employee['BS']*(.2)
        employee['MA'] = employee['BS']*(.15)
        employee['PFD'] = employee['BS']*(.05)
        calculated_data.append(employee)
    return calculated_data

print("(a)")
for i in calculateSalary(employe_data):
    print(i)


def UpdateSalary(data):
    data = [{'Name': employees['Name'], 'BS' : (employees['BS'] + employees['BS']*.05)} for employees in data]
    # print(data)
    return data

print("(b)")
for j in calculateSalary(UpdateSalary(employe_data)):
    print(j)

print("(c)")
def calculate_final(data):
    for employee in data:
        print(f"Employee: {employee['Name']} Total Salery: {employee['BS'] + employee['HA'] + employee['MA'] - employee['PFD']}")


calculate_final(calculateSalary(employe_data))