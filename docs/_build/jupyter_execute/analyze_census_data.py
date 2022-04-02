#!/usr/bin/env python
# coding: utf-8

# # Analyzing Education's effect on Time Spent Working

# ## Summary:
# Our group aims to analyze and determine the correlation between the number of years an individual spends in school compared to how long they spend working every week. We download and clean the data, then perform a linear regression analysis to find the relationship that holds between the two.

# ## Introduction:
# Education is often seen as a gateway to greater understanding of the world; it is also seen as a way to gain freedom from having to work low paying jobs to pay living expenses. We aim to determine the extent of this view and track how these expectations work in reality. We also use our results to predict the number of hours worked with different kinds of higher education degrees.
# 
# For this project, we use the "Census Income" dataset from the UC Irvine Machine Learning Repository, representing data from the 1994 US Census. For more details, see the original source here: https://archive-beta.ics.uci.edu/ml/datasets/adult

# ## Methods & Results:

# --------------------
# 
# ### Code:

# #### Imports

# We use the pandas library for storing and processing data, the numpy data for more detailed analytical functions, and the matplotlib library to plot our findings. We inlude several functions we created in the Python folder.

# In[1]:


from myst_nb import glue
import sys
import pandas as pd
sys.path.append("..")
from src.regression import regression
from src.filter import filter as fil
from src.remove_column import remove_column


# #### Data 
# 
# Data is stored in a 4mb .data file from https://archive-beta.ics.uci.edu/ml/datasets/census+income, which functions as a .csv file. The column names, as well as other information on the dataset, are in the accompanying .names file. 

# In[2]:


data = pd.read_csv('../data/adult.data')
data_head = data.head()

glue("data_head", data_head)


# ```{glue:figure} data_head
# :figwidth: 800px
# :name: "dataset"
# Cleaned dataset
# ```

# ```{glue:} data
# ```

# The education-num data is not the years spent in formal education, but an ordinal representation of the education category. Matching the values by counting the number of occurrences in the data, we can find the intended pairs:

# In[3]:


legend = pd.DataFrame({'Number':["Meaning"],
'1':["Preschool"],
'2':["1st-4th"],
'3':["5th-6th"],
'4':["7th-8th"],
'5':["9th"],
'6':["10th"],
'7':["11th"],
'8':["12th"],
'9':["HS-grad"],
'10':["Some-college"],
'11':["Assoc-voc"],
'12':["Assoc-adm"],
'13':["Bachelors"],
'14':["Masters"],
'15':["Prof-school"],
'16':["Doctorate"],})
glue("legend", legend)


# ```{glue:figure} legend
# :figwidth: 800px
# :name: "legend"
# Education Numbers Meaning
# ```

# ```{figure} ../data/ed_hours_plot.png
# ---
# height: 300px
# name: ed_hours_plot
# ---
# Level of Education vs Hours Worked per Week (All individuals)
# ```

# In[4]:


ed = data['education-num']
hours = data['hours-per-week']
m, b = regression(ed, hours)
preschool = round(m*1+b, 2)
bachelors = round(m*13+b, 2)
doctorates = round(m*16+b, 2)
three_doctorates = round(m*20+b, 2)

# Only preschool
glue("preschool", preschool)
# bachelors
glue("bachelors", bachelors)
# doctorates
glue("doctorates", doctorates)
# 1 education-num is close to 2 years in school at the end of the scale. So, 20 is equivalent to 3 doctorates:
glue("3_doctorates", three_doctorates)


# ```{figure} ../data/canada_plot.png
# ---
# height: 300px
# name: canada_plot
# ---
# Level of Education vs Hours Worked per Week (Canadians only)
# ```

# In[5]:


data_canada = pd.read_csv('../data/adult.data_canada.data')
ed_canada = data_canada['education-num']
hours_canada = data_canada['hours-per-week']
m, b = regression(ed_canada, hours_canada)
preschool_canada = round(m*1+b, 2)
bachelors_canada = round(m*13+b, 2)
doctorates_canada = round(m*16+b, 2)
three_doctorates_canada = round(m*20+b, 2)

# Only preschool
glue("preschool_canada", preschool_canada)
# bachelors
glue("bachelors_canada", bachelors_canada)
# doctorates
glue("doctorates_canada", doctorates_canada)
# 1 education-num is close to 2 years in school at the end of the scale. So, 20 is equivalent to 3 doctorates:
glue("3_doctorates_canada", three_doctorates_canada)


# ```{figure} ../data/usa_plot.png
# ---
# height: 300px
# name: usa_plot
# ---
# Level of Education vs Hours Worked per Week (Americans only)
# ```

# In[6]:


data_usa = pd.read_csv('../data/adult.data_usa.data')
ed_usa = data_usa['education-num']
hours_usa = data_usa['hours-per-week']
m, b = regression(ed_usa, hours_usa)
preschool_usa = round(m*1+b, 2)
bachelors_usa = round(m*13+b, 2)
doctorates_usa = round(m*16+b, 2)
three_doctorates_usa = round(m*20+b, 2)

# Only preschool
glue("preschool_usa", preschool_usa)
# bachelors
glue("bachelors_usa", bachelors_usa)
# doctorates
glue("doctorates_usa", doctorates_usa)
# 1 education-num is close to 2 years in school at the end of the scale. So, 20 is equivalent to 3 doctorates:
glue("3_doctorates_usa", three_doctorates_usa)


# In[7]:


df = pd.DataFrame({"":["Preschool", "Bachelors", "Doctorate", "3 Doctorates"], 
"All individuals":[preschool, bachelors, doctorates, three_doctorates], 
"Canadians":[preschool_canada, bachelors_canada, doctorates_canada, three_doctorates_canada],
"Americans":[preschool_usa, bachelors_usa, doctorates_usa, three_doctorates_usa]})
glue("df", df)


# ```{glue:figure} df
# :figwidth: 600px
# :name: "table"
# Level of education vs population subsets
# ```

# ## Discussion:
# 
# Looking at {numref}`ed_hours_plot`, we can that there is a positive correlation between education level and hours worked. Someone with minimal education would likely not have a full time job (i.e preschool has an estimate of {glue:text}`preschool` hours worked, and people with bachelors or doctorates tend to work slightly more ({glue:text}`bachelors` and {glue:text}`doctorates` hours worked respectively) (This could be due to most working exactly 40, and some working many more). Following the trend to a higher number like 20, a rough equivalent of 3 PhDs, brings us to an estimate of {glue:text}`3_doctorates` hours worked a week.
# 
# There are many possible explanations as to why this exists. One possibility is that this is caused by students still in school, who have low education levels and would only work part time. Another is that jobs with lower education requirements do not allow for advancement to full time work, or that jobs with higher requirements are more demanding. 
# 
# However we can also see that our predictive model is misleading as the model predicts that pre-school kids work {glue:text}`preschool` hours per week. We know that this is incorrect. This does not mean that people in pre-school work {glue:text}`preschool` hours a week but that people that only completed pre-school and nothing else sometime in the past now work that many hours. 
# 
# Looking at the graphs for Canadians ({numref}`canada_plot`) and Americans ({numref}`usa_plot`) only, we can see that there actually is a negative correlation between hours worked and education level. This can be because at higher education levels you may still be spending a lot of time studying rather than learning hence your hours stay the same. The working hours for education level are almost consistent at 40hrs which is the standard full time job in Canada and USA hence it makes sense that it is consistent with all education levels as it just means everyone is working standard full time hours.
# 
# Analyzing other variables in this data-set such as age could offer hints as to which explanation is correct. To be certain and to distinguish if this is truly causation or just correlation would likely require gathering more detailed data from other sources.

# ## References:

# {cite}`bick_2018, boswell_2013, causa_2008, heckman_2011`

# ```{bibliography}
# :filter: docname in docnames
# ```
