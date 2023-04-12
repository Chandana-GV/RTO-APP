# Report 1: Compliance by Employee
import openpyxl

# Create a new workbook and worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.create_sheet('Compliance by Employee')

# Add headers to the worksheet
worksheet.append(['Employee ID', 'Employee Name', 'Compliance Type', 'Start Date', 'End Date'])

# Add data to the worksheet
worksheet.append(['12345', 'John Doe', 'Work from home', '2023-04-05', '2023-04-05'])
worksheet.append(['23456', 'Jane Smith', 'Work from office', '2023-04-06', '2023-04-08'])

# Save the workbook
workbook.save('Employee sample data.csv')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from excel file
df = pd.read_excel('Employee sample data.csv', sheet_name='Compliance by Employee')

# Group data by Manager and Date
grouped_df = df.groupby(['Manager', 'Date'], as_index=False)['Compliance'].sum()

# Plot compliance by manager
sns.set_style("darkgrid")
g = sns.FacetGrid(grouped_df, col="Manager", col_wrap=3)
g.map(sns.lineplot, "Date", "Compliance")

# Show the plot
plt.show()

