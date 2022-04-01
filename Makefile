# download data, process, and plot it
all : data/adult.data data/adult.data_unprocessed.data data/adult.data_usa.data data/adult.data_canada.data data/ed_hours_plot.png data/canada_plot.png data/usa_plot.png

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

# remove all created files
clean:
	rm -f data/adult.data data/adult.data_unprocessed.data data/ed_hours_plot.png data/canada_plot.png data/usa_plot.png