# DSCI-310-Group-3

Analyzing Education's Effect on Hours Worked

Contributors: Alex Khadra, Damien Fung, Ryan Lazenby


## Summary:

This project looks into US 1994 census data to investigate the effects of higher education, and hours worked. We come up with a predictive model that estimates the amount of hours worked per week based on the amount of years of education.

Our data set includes columns:

- **age** Current age of person
- **workclass** In what sector their occupation is in
- **fnlwgt** A weighting variable calculated by the Census Bureau 
- **education** Current level of education
- **education-num** How many years of education
- **marital-status** Whether a person is married or not
- **occupation** Person occupation 
- **relationship** Current relationship (Ex. not-in family, husband, wife)
- **race** Persons race
- **sex** Persons sex
- **capital-gain** Amount of capital gain a person has
- **capital-loss** Amount of capital loss a person has
- **hours-per-week** Hours worked per week
- **native-country** Persons native country
- **income** Income level

The code needed to run the analysis is included in the analysis.ipynb file, and the required dependencies to obtain our results are:

- numpy=1.22.2
- matplotlib=3.5.1
- pandas=1.4.1

Through our analysis, as seen in the `analyze_census_data.ipynb` we can that there is a positive correlation between education level and hours worked. Someone with minimal education would likely not have a full time job, and people with bachelors or doctorates tend to work slightly more (This could be due to most working exactly 40, and some working many more). Following the trend to a higher number like 20, a rough equivalent of 3 PhDs, 

There are many possible explanations as to why this exists. One possibility is that this is caused by students still in school, who have low education levels and would only work part time. Another is that jobs with lower education requirements do not allow for advancement to full time work, or that jobs with higher requirements are more demanding. 

Analyzing other variables in this data-set such as age could offer hints as to which explanation is correct. To be certain and to distinguish if this is truly causation or just correlation would likely require gathering more detailed data from other sources.


## Usage
The analysis used in this project can be reproduced through Docker.
- Install git
- Clone this git repository by using one of the following methods in terminal:
    - `git clone git@github.com:DSCI-310/DSCI-310-Group-3.git`
    - `git clone https://github.com/DSCI-310/DSCI-310-Group-3.git`
    - **OR** pasting either `git@github.com:DSCI-310/DSCI-310-Group-3.git` or `https://github.com/DSCI-310/DSCI-310-Group-3.git` into a git version control interface
- Install Docker
- Navigate to the root of this project
- To run this project non-interactively, run the following command in your terminal
`docker run -it --rm -p 8888:8888 -v "/$(pwd):/home/education-hours-worked" fungd2/dsci-310-group-3 make - C /home/education-hours-worked all`
- To reset the analysis run the following command in your terminal
`docker run -it --rm -p 8888:8888 -v "/$(pwd):/home/education-hours-worked" fungd2/dsci-310-group-3 make - C /home/education-hours-worked clean`

The code can be tested by running `pytest tests` from the main directory. As several pandas functions return warnings due to deprecations or to specify their usage, some of the tests that pass are noted as returning these warnings instead.

This project uses the MIT license for its code and the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) license for the analysis.
