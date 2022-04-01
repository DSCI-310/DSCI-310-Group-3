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

# #### Data 
# 
# Data is stored in a 4mb .data file from https://archive-beta.ics.uci.edu/ml/datasets/census+income, which functions as a .csv file. The column names, as well as other information on the dataset, are in the accompanying .names file. 

# ```{code-cell} ipython3
# 
# import pandas as pd
# data = pd.read_csv(adult.data)
# data.head()
# ```

# The education-num data is not the years spent in formal education, but an ordinal representation of the education category. Matching the values by counting the number of occurrences in the data, we can find the intended pairs:

# **Education Numbers Meaning**:
# 
# |Number|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**|**15**|**16**| 
# |------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|------|------|------|------|------|------|
# |Meaning|Preschool|1st-4th|5th-6th|7th-8th|9th|10th|11th|12th|HS-grad|Some-college|Assoc-voc|Assoc-acdm|Bachelors|Masters|Prof-school|Doctorate|

# ```{figure} ../data/ed_hours_plot.png
# ---
# height: 300px
# name: ed_hours_plot
# ---
# Level of Education vs Hours Worked per Week
# ```

# ```{figure} ../data/canada_plot.png
# ---
# height: 300px
# name: canada_plot
# ---
# Level of Education vs Hours Worked per Week (Canadians only)
# ```

# ```{figure} ../data/usa_plot.png
# ---
# height: 300px
# name: usa_plot
# ---
# Level of Education vs Hours Worked per Week (Americans only)

# In[1]:



# TODO: EMBED PRESECHOOL, BACHELORS, DOCTORATES AND 3 DOCTORATES INLINE


# ## Discussion:
# 
# Looking at {numref}`ed_hours_plot`, we can that there is a positive correlation between education level and hours worked. Someone with minimal education would likely not have a full time job, and people with bachelors or doctorates tend to work slightly more (This could be due to most working exactly 40, and some working many more). Following the trend to a higher number like 20, a rough equivalent of 3 PhDs, brings us to an estimate of 47.49 hours worked a week.
# 
# There are many possible explanations as to why this exists. One possibility is that this is caused by students still in school, who have low education levels and would only work part time. Another is that jobs with lower education requirements do not allow for advancement to full time work, or that jobs with higher requirements are more demanding. 
# 
# However we can also see that our predictive model is misleading as the model predicts that pre-school kids work 33.98 hours  per week. We know that this is incorrect. This does not mean that people in pre-school work 33.98 hours a week but that people that only completed pre-school and nothing else sometime in the past now work that many hours. 
# 
# Looking at the graphs for Canada ({numref}`canada_plot`) and USA ({numref}`usa_plot`) only, we can see that there actually is a negative correlation between hours worked and education level. This can be because at higher education levels you may still be spending a lot of time studying rather than learning hence your hours stay the same. The working hours for education level are almost consistent at 40hrs which is the standard full time job in Canada and USA hence it makes sense that it is consistent with all education levels as it just means everyone is working standard full time hours.
# 
# Analyzing other variables in this data-set such as age could offer hints as to which explanation is correct. To be certain and to distinguish if this is truly causation or just correlation would likely require gathering more detailed data from other sources.

# ## References:

# ```{bibliography}
# :style: unsrtalpha
# :filter: docname in docnames
# ```

# 
