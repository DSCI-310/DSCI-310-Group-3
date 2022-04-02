# download data, process, and plot it
all : data/adult.data data/adult.data_unprocessed.data data/adult.data_usa.data data/adult.data_canada.data data/ed_hours_plot.png data/canada_plot.png data/usa_plot.png docs/_build/html/index.html

# download data
data/adult.data : src/download_data.py
	python ./src/download_data.py https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data ./data/adult.data

# process data
data/adult.data_unprocessed.data data/adult.data_canada.data data/adult.data_usa.data : data/adult.data src/process_data.py
	python ./src/process_data.py data/adult.data

# make education vs hours per week plot
data/ed_hours_plot.png : data/adult.data src/visualize_data.py
	python ./src/visualize_data.py ./data/adult.data ./data/ed_hours_plot.png education-num hours-per-week
    
# make Canada specific education vs hours per week plot
data/canada_plot.png : data/adult.data_canada.data src/visualize_data.py
	python ./src/visualize_data.py ./data/adult.data_canada.data ./data/canada_plot.png education-num hours-per-week
    
# make USA specific education vs hours per week plot
data/usa_plot.png : data/adult.data_usa.data src/visualize_data.py
	python ./src/visualize_data.py ./data/adult.data_usa.data ./data/usa_plot.png education-num hours-per-week

# render Jupyter Book report in HTML
docs/_build/html/index.html: docs/_config.yml docs/_toc.yml docs/analyze_census_data.ipynb docs/references.bib
	jb build docs/

# remove all created files
clean:
	rm -f data/adult.data data/adult.data_unprocessed.data data/ed_hours_plot.png data/canada_plot.png data/usa_plot.png