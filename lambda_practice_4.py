# 4. Write a Python program to sort a list of dictionaries using Lambda. Go to the editor
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
list_dictionaries = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
                     {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
                     {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
list_dictionaries.sort(key=lambda x: x["make"])
print(list_dictionaries)
