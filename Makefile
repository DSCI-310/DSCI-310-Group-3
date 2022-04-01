# download data, process, and plot it
all : data/adult.data data/adult.data_unprocessed.data data/ed_hours_plot.png

# download data
data/adult.data : src/download_data.py
	python ./src/download_data.py https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data ./data/adult.data

# process data
data/adult.data_unprocessed.data : data/adult.data src/process_data.py
	python ./src/process_data.py data/adult.data

# make education vs hours per week plot
data/ed_hours_plot.png : data/adult.data src/visualize_data.py
	python ./src/visualize_data.py ./data/adult.data ./data/ed_hours_plot.png education-num hours-per-week

# remove all created files
clean:
	rm -f data/adult.data data/adult.data_unprocessed.data data/ed_hours_plot.png