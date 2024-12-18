import pandas as pd

#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
# print(df)

#Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]
# print(x)
#check the type of x
# print(type(x))

#Retrieving the Department, Salary and ID columns and assigning it to a variable z

z = df[['Department','Salary','ID']]
# print(z)

student_list = {
    "Student" : ['David', 'Samuel', 'Terry', 'Evan'], 
    "Age": [27, 24, 22, 32],
    "Country":["UK", "Canada", "China", "USA"],
    "Course":['Python', "Data Structures", "Machine Learning", "Web Development"],
    "Marks":[85, 72, 89, 76]
}

student_data_frame = pd.DataFrame(student_list)
b = student_data_frame['Student']
c = student_data_frame[['Country', "Course"]]


# print(student_data_frame)
# print(b)
# print(c)

# Access the value on the first row and the first column

# print(student_data_frame.iloc[0, 0])

# Access the column using the name

print(df.loc[3, 'Salary'])