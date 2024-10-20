

personal_info = {
    'name': 'Ashok',
    'address' : 'Arghakhanci',
    'salary' : 120000

}

# copy garyo vane naya reference banxa, if personal_info_new = personal_info garyo vane
# puranai dictionary lai personal_info_new le tei same dictionary ko reference linxa
personal_info_new = personal_info.copy()

print(personal_info_new)