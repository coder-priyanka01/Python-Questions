# Take user input age and check what datatype it is. Convert it to integer and multiply it by 10. Print the result.

age = input("Enter your age: ")
print(type(age))  # Check the datatype of age 

age_int = int(age)  # Convert age to integer
result = age_int * 10  # Multiply by 10
print(result)  # Print the result    