# 2. Write a Python script to add a key to a dictionary. Go to the editor
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
Add_items = {7: "abhay", 9: "sonu", 1: "sonuy", 6: "python", 2: "deepak"}
Add_items.setdefault(10, "java")
print(Add_items)
