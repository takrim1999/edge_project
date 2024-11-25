fruit_list = ['Apple','Banana','Cherry','pineapple']
print(fruit_list)
print("First Element: ", fruit_list[0])
print("Last Element:" , fruit_list[-1])
fruit_list.append('Orange')
fruit_list.insert(fruit_list.index('Banana')+1,'Grape')
print(fruit_list)
fruit_list[0] = 'kiwi'
fruit_list.remove('Banana')
print(fruit_list)