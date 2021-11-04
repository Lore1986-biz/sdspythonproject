#!/usr/bin/env python
# coding: utf-8

# # Module: Coding for Data Analysis
# **💪 The Challenge**  
# You were recently hired by the City of Chicago as a data analyst to support the Finance Department. For your first project on the job, the Head of Finance (who has minimal data experience) asked you to send a summary via email answering the following questions:
# 
# 1. Does the City of Chicago pay more for salary or hourly employees among those who are full-time?
# 2. What's the distribution of pay, among City of Chicago employees, stratified by hourly and salary employees?
# 3. What are the top 5 highest paid departments by total and employee average?
# 
# **💡 Hint:**  
# Pay is split up by yearly salary employees and hourly employees. Consider how you can potentially compare the pay among these two types of workers.
# 
# #hourly employees: you are paid on work hours
# 
# #how you can potentially compare the pay among these two types of workers.
# 
# 1) Get the average work hours in a week in the U.S https://www.statista.com/statistics/215643/average-weekly-working-hours-of-all-employees-in-the-us-by-month/ : it's 35 hours per week
# 
# 2) Multiply per 52 weeks: 1820 hours in a year
# 
# 
# **💻 Industry Perspective**  
# This module with mimic similar requests you will receive as a data analyst. While doing this module you should constantly consider how your work will be communicated to non-technical stakeholders.
# 
# **📝 Module Structure**  
# This will be split up into two modules for each week:
# - Week 1: Exploratory Data Analysis
#     - Reviewing data
#     - Plotting Histograms
#     - Writing a high level analysis plan
# - Week 2: Data Cleaning and Insights
#     - Data cleaning
#     - Feature engineering a total yearly pay variable
#         - "Feature engineering" can be understood as creating new variables from existing data.
#     - Answering the above questions
# 
# **🚨 Note:**  
# This data sourced from the [City of Chicago's government website](https://data.cityofchicago.org/Administration-Finance/Current-Employee-Names-Salaries-and-Position-Title/xzkq-xp2w). For the purpose of this module, the provided CSV has altered data to provide a more realistic challenge for data cleaning.
# 
# **🐍 Python A-Z: Helpful Modules:**  
# - Module 2 - Core Programming Principles
#     - Types of Variables
#     - The "For" Loop
#     - The "If" statement
# - Module 3 - Fundamentals of Python
#     - Let's create some lists
#     - Slicing
#     - Slicing Arrays
# - Module 4 - Matrices
#     - Dictionaries in Python
# - Module 5 - Data Frames
#     - The entire module
# - Module 6 - Advanced Visualization
#     - What is a Category data type?
#     - Histograms
#     - Violinplots vs Boxplots

# # Week 1: Exploratory Data Analysis
# The focus of week 1 will be on:
# 1. The general steps of reviewing a data for a project via python (e.g. summaries and histograms).
# 2. Creating a high level analysis plan to guide your work for week 2.  
# 
# **💻 Industry Perspective**  
# These steps are the foundation of any data project you will work on, and will help set you up for success. Specifically, taking this steps early can give you an idea of the scope of a requested project and whether it aligns with the expectations of the requester.

# ### Import Packages

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt


# If you are running this notebook from Colab, uncomment and run this cell first (this will give access to the dataset to Colab notebook, [more info here](https://www.geeksforgeeks.org/ways-to-import-csv-files-in-google-colab/))

# In[ ]:


#import io
#from google.colab import files
#uploaded = files.upload()


# ### Import Data

# ---
# **❓ 1. Import the CSV named `chicago_employee_salary_edited.csv` and show the first 5 rows of the imported dataframe.**

# In[ ]:


stats=pd.read_csv('C:\\Users\\LorenzoBini\\Desktop\\Python Course\\Project\\chicago_employee_salary_edited.csv')
stats.head()


# ### Reviewing Data

# ---
# **❓ 2. Return the names of all the columns within the dataframe using pandas.**  
# 
# Though there are not that many columns, pulling this information programmatically is useful if we ever want to use the column names in a function or for-loop.

# In[ ]:


stats.columns


# ---
# **❓ 3. Determine the data types of every column within the dataframe using pandas.**  
# 
# Ensuring the correct data types is an important data quality step that will prevent error messages later in the process.
# 
# 🐍 Python A-Z: Module 5

# In[ ]:


stats.info()


# ---
# **❓ 4. Determine how many rows and columns are present within the dataframe.**

# In[ ]:


print ("There are:" + " "+str(len(stats))+" "+"rows"+ " "+ "and"+" " + str(len(stats.columns))+" "+"columns" " "+"in this table 'stats'")


# ---
# **❓ 5. Determine the count of NAs present for each column within the dataframe.**  
# 
# **💭 Reflection Point:**  
# Are NAs always bad to have in your data? In the context of this dataframe, think of some instances where 1) NAs would be acceptable to have present, and 2) NAs would not be acceptable.

# In[ ]:


stats.isna().sum()


# ---
# **❓ 6. For each variable that is a continuous variable, provide the summary statistics including the mean, min, and max.**  
# 
# **💡 Hint:**  
# Pandas can pull all this information with a single function.

# In[ ]:


stats.describe()


# ---
# **❓ 7. For each variable that is a continuous variable, create a histogram to view its respective distribution**
# 
# **💡 Hint:**  
# Check out the [pandas hist() function](https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.DataFrame.hist.html).

# In[ ]:


ContinuosVariable= ['TypicalHours', 'AnnualSalary', 'HourlyRate']
stats.[ContinuosVariable].hist(
    bins=40
    layout=(1,3)
    figsize=(15,5)
)


# ---
# **❓ 8. For each variable that is not a continuous variable (e.g. text data), determine:**
# - **a) the number of values present**
# - **b) the number of unique values present**  
# - **c) each unique value if there are less than 100 unique values.**

# In[ ]:


col_name=['Name', 'JobTitles', 'Department', 'FullOrPartTime',
       'SalaryOrHourly'] 

for i in col_name: 
unique_values= sorted(stats[cols].unique)
num_unique_values= len (unique_values) 
print (
'Column:'+{col}+'NumberOfValues:'+{num_values}+'NumberOfUniqueValues'+{num_unique_values}

)

if stats.Name.nunique()<100:
    print(unique_values)
    else print("Too many unique values")


# ---
# **❓ OPTIONAL: Using this notebook's markdown cells, write a brief data analysis plan based off the data review you just conducted above using the following template.**  
# - **Data Source**
#     - Describe the data source at a high level in 1 to 2 sentences.
# - **Data Preparation**
#     - What are the main data cleaning steps and data quality checks do you need to conduct before you can analyze the data.
# - **Data Analysis**
#     - For each of the questions asked by the Head of Accounting, describe how you will derive the answer.
# 
# **💡 Hint:**  
# Checkout the [documentation](https://www.markdownguide.org/basic-syntax/) if you are new to markdown.
# 
# **💭 Reflection Point:**  
# Why might it be useful to create an analysis plan before going directly into analyzing your data? How could a data analysis plan help you work better with your non-technical stakeholders?

# ### Your Markdown Here
# .  
# .  
# .  

# # Week 2: Data Cleaning and Insights
# The focus of week 2 will be on:
# - Cleaning data and thinking through assumptions when preparing data.
# - Feature engineering a total yearly pay variable.
# - Answering the questions presented by the Head of Finance.
# 
# **💻 Industry Perspective**  
# Along with the technical skills, being able to make great assumptions about your data is key to success as a data professional. Your assumptions need to be documented and validated by external sources (e.g. a subject matter expert or personal research) when possible. Having thoughtful assumptions and being able to clearly communicate these steps will build trust in your results from your stakeholders.

# ### Data Preparation

# **💭 Reflection Point:**  
# One of the first steps we are going to take is copying our dataframe under a new name. Why would it be important to take this step? Are there any instances where we wouldn't want to take this step?

# In[ ]:


salary_clean_df = stats.copy()


# ---
# **❓ 9. `Full or Part-Time` is important to answer the Head of Finance's questions, thus please review this variable to ensure it's clean.**  
# 
# **💡 Hints:**  
# 1. Use `sorted(salary_df[<col_name>].unique())` to check your work.
# 2. `pandas.Series.str.replace` can be useful for this task.
#     - Documentation: https://pandas.pydata.org/docs/reference/api/pandas.Series.str.replace.html
# 
# **🐍 Python A-Z: Helpful Modules:** 
# - Replace and dealing with nulls explained:
#     - https://www.superdatascience.com/courses/data-manipulation-in-python/replacing-and-thresholding
# - Vectorized function (str) explained:(6:07)
#     - https://www.superdatascience.com/courses/data-manipulation-in-python/apply-map-and-vectorised-functions

# In[ ]:


salary_clean_df["FullOrPartTime"].replace("F", "Full-Time", regex=True)
salary_clean_df["FullOrPartTime"].replace("Full", "Full-Time", regex=True)
salary_clean_df["FullOrPartTime"].replace("P", "Part-Time", regex=True)
sorted (salary_clean_df['Full or Part-Time'].unique())


# ---
# **❓ 10. Another important variable is `Department`. Please review this variable as well to ensure it is clean.**  
# 
# **💭 Reflection Point:**  
# Sometimes we don't have all the data we need to make the best possible assumptions, and thus we need to get creative to answer our questions. For example, I used the [City of Chicago's department list website](https://www.chicago.gov/city/en/depts.html) to validate some of my assumptions. What are some other ways we can check assumptions?

# In[ ]:


#Dictionary to map value to replace
replacement_mapping_dict_department = {
    'ADMIN_HEARNG': 'ADMIN HEARNG',
    'ANIMALCONTRL': 'ANIMAL CONTRL',
    'ANIMAL_CONTRL': 'ANIMAL CONTRL',
    'BUDGET AND MGMT': 'BUDGET & MGMT',
    'FAMILY AND SUPPORT': 'FAMILY & SUPPORT',
    'FAMILY SUPPORT': 'FAMILY & SUPPORT',
    'HOUSING': 'HOUSING & ECON DEV',
    'MAYORS OFFICE': "MAYOR'S OFFICE",
    'POLICE' : 'POLICE DEPT',
    'POLICE BOARD': 'POLICE DEPT',
    'PUBLIC_LIBRARY':'PUBLIC LIBRARY',
    'STREETS SAN':'STREETS & SAN',
    'WATER_MGMNT': 'WATER MGMNT',
    'admin hearng':'ADMIN_HEARNG',
    'aviation': 'AVIATION',
    'buildings':'BUILDINGS',
    'finance': 'FINANCE',
    'police': 'POLICE',
    'streets and san':'STREETS & SAN'   
    
}

#replacement code
salary_clean_df["Department"].replace(replacement_mapping_dict_department)


# ---
# **❓ 11. We now need to ensure the variables around pay are in a good enough state to do our analysis. First, check the variable `Typical Hours` for any discrepancies we can resolve.**
# 
# **💡 Hints:**  
# 1. Your manager informed you that there was a clerical error where a certain department accidentally added a extra zero to their full-time workers' typical hours.
# 2. Use `np.nan` to create Null values.
# 3. Use `pd.DataFrame.loc` to subset and filter your data.
#     - Documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
#     - Note that `.loc` is for accessing several elements while `.at` accesses a single element within a dataframe.
# 
# **💭 Reflection Point:**  
# We are going to make some assumptions if we make any data cleaning changes. How would this impact our analysis? How can we best communicate these assumptions with non-technical stakeholders?

# In[ ]:


#Use np.nan to create Null Values
salary_clean_df['Typical Hours'] = salary_clean_df['Typical Hours'].replace(np.nan, None)
salary_clean_df.loc[salary_clean_df[:,'Typical Hours']=35.0


# ---
# **❓ 12. Now let's check the variables `Hourly Rate` and `Annual Salary` for any discrepancies.**
# 
# **💡 Hints:**  
# - Check histograms and summary statistics.
# - Identify pattern and resolve the error using this pattern to your advantage.
# - Check histograms and summary statistics again to confirm your change worked.

# In[ ]:


salary_clean_df['Hourly Rate']=salary_clean_df.loc[:,'Hourly Rate']=salary_clean_df['Annual Salary']/1820


# ---
# **❓ 13. Now, let's confirm whether or not the nulls present are valid.**  
# 
# **💡 Hint:**  
# What are two conditions that can't be true together for `Salary or Hourly` and `Annual Salary`?

# In[ ]:


# What are two conditions that can't be true together for Salary or Hourly and Annual Salary?
#Where it's full-time job, typical hours can't be hourly and  Annual Salary is expressed in 10,20


# ---
# **❓ 14. Create a column called `Yearly Pay` that allows us to compare both salary and hourly employees' pay within the same column.**
# 
# **💡 Hints:**  
# - There are 52 weeks within a year.
# - You can use pandas to multiply or add columns together to create values within a new column (i.e. "vectorization")

# In[ ]:


salary_clean_df['YearlyPay']=(salary_clean_df.TypicalHours*salary_clean_df.HourlyRate)*52


# ### Data Analysis  
# Again, we are going to copy our data for the next steps.

# In[ ]:


salary_analysis_df = salary_clean_df.copy()


# ---
# **❓ 15. Does the City of Chicago pay more for salary or hourly employees among those who are full-time?**

# In[ ]:


##################
# your code here #
##################


# ---
# **❓ 16. What's the distribution of pay, among City of Chicago employees, stratified by hourly and salary employees?**
# 
# How to Plot a Histogram  
# https://seaborn.pydata.org/generated/seaborn.displot.html
# ```
# # plot histogram
# sns.displot(kind='hist', data=<data_frame>, x=<column_name>, hue=<column_name>, height=4, aspect=4)
# ```
# 
# How to Plot a Boxplot  
# https://seaborn.pydata.org/generated/seaborn.boxplot.html
# ```
# # plot boxplot
# plt.pyplot.figure(figsize=(20,5))
# sns.boxplot(data=<data_frame>, x=<column_name>, y=<column_name>)
# ```
# 
# 💭 Reflection Point: 
# What's the difference between a boxplot and histogram? Which graph type best communicates our results?

# In[ ]:


##################
# your code here #
##################


# ---
# **❓ 17. What are the top 5 highest paid departments by total and employee average?**
# 
# 💭 Reflection Point:  
# What are the implications of using mean as compared to median?
# 
# **🐍 Python A-Z: Helpful Modules:** 
# - Groupby explained:
#     - https://www.superdatascience.com/courses/data-manipulation-in-python/basic-grouping-syntax
# - `groupby().agg()` explained:
#     - https://www.superdatascience.com/courses/data-manipulation-in-python/grouping-aggregation

# In[ ]:


##################
# your code here #
##################


# ---
# **❓ 18. Congrats on completing your first analysis at your new job-- you are already driving impact! As a final step, write an email to the Head of Finance answering their questions. Remember that this stakeholder has minimal data experience.**

# ### Your Email Here
# .  
# .  
# .  

# ---
# **🔥 Hard Challenge 🔥**  
#   
# **❓ OPTIONAL: The Head of Finance loved your work so much that you were asked to generate your results every quarter. Create a function, or set of functions, to automate this entire analysis.**
# 
# **💡 Hint:**  
# Do not attempt this until you have completed the rest of the module.  
# 
# **💻 Industry Perspective**  
# In industry, you often take your raw code from an initial analysis and "refactor" it for scalability.*

# In[ ]:


##################
# your code here #
##################


# # End of Module
# *Disclaimer:  
# This site provides applications using data that has been modified for use from its original source, www.cityofchicago.org, the official website of the City of Chicago.  The City of Chicago makes no claims as to the content, accuracy, timeliness, or completeness of any of the data provided at this site.  The data provided at this site is subject to change at any time.  It is understood that the data provided at this site is being used at one’s own risk.*
