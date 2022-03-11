# DSCI-310-Group-3

Analyzing Education's Effect on Capital Gains

Contributors: Alex Khadra, Damien Fung, Ryan Lazenby


## Summary:

This project looks into US 1994 census data to investigate the effects of higher education, and education in general, on a person's reported capital gains.

The code needed to run the analysis is included in the analysis.ipynb file, and the required dependencies to obtain our results are:

- numpy=1.22.2
- matplotlib=3.5.1
- pandas=1.4.1

Through oour analysis, as seen in the `analyze_census_data.ipynb` we can that there is a positive correlation between education level and hours worked. Someone with minimal education would likely not have a full time job, and people with bachelors or doctorates tend to work slightly more (This could be due to most working exactly 40, and some working many more). Following the trend to a higher number like 20, a rough equivalent of 3 PhDs, 

There are many possible explanations as to why this exists. One possibility is that this is caused by students still in school, who have low education levels and would only work part time. Another is that jobs with lower education requirements do not allow for advancement to full time work, or that jobs with higher requirements are more demanding. 

Analyzing other variables in this dataset such as age could offer hints as to which explanation is correct. To be certain and to distinguish if this is truly causation or just correlation would likely require gathering more detailed data from other sources.


## Usage
The analysis used in this project can be reproduced through Docker.
- Install Docker
- Navigate through terminal to the root director of this project
- Run the following commands to run the Docker container:
    - `docker pull fungd2/dsci-310-group-3`
    - `docker run --rm -p 8787:8787 -e PASSWORD="password" fungd2/dsci-310-group-3`
- go to http://localhost:8787 to use the project's notebook

This project uses the MIT license for its code and the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) license for the analysis.