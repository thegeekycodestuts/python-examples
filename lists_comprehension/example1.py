# 

# Python List Comprehension
numbers = [5, 10, 22, 35, 55]
dividedlist = [num / 5 for num in numbers]
print(dividedlist)

# for loop example
dividedlist = []
for num in numbers:
    dividedlist.append(num / 5)
print(dividedlist)

# filtering numbers
scores = [85, 92, 78, 95, 88, 72, 98]
passing_scores = [score for score in scores if score >= 80]
print(passing_scores)

# Creating Transformed Lists
words = ['hello', 'world', 'python', 'list', 'comprehension']
capitalized_words = [word.capitalize() for word in words]
print(capitalized_words)

# Conditional Mapping
scores = [85, 92, 78, 95, 88, 72, 98]
result_categories = ['Pass' if score >= 80 else 'Fail' for score in scores]
print(result_categories)


# Nested List Comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_matrix = [num for row in matrix for num in row]
print(flattened_matrix)
