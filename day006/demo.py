cities={
    'INDIA':'PUNE',
    'LANKA':'COLOMBO',
    'BANGLADESH':'DHAKA'

}

best=cities['INDIA']
print(best)

worst=cities.get('BANGLADESH')
print(worst)

update1=cities['LANKA']='MALINGA'
print(update1)

print(cities)

cities.update({'USA':'DC',
                       'UK':'LONDON'})
print(cities)

del cities['INDIA']
print(cities)

