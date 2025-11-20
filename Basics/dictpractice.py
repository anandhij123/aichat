student_dict={"John":25,"Jane":22,"Doe":23,"Alice":24}
print(type(student_dict))
print(student_dict)
# Fetch the names and sort in ascending order without using sort operator
list_names=list(student_dict.keys())
print (sorted(list_names))
list_age=list(student_dict.values())
print (sorted(list_age))
sorted_dict= dict (sorted(student_dict.items())) # sorting dictionary by keys
print (sorted_dict)
# Sorting dictionary by values
sorted_by_values=dict(sorted(student_dict.items(), key=lambda item: item[1]))
print(sorted_by_values)
