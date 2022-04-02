FROM jupyter/base-notebook:notebook-6.4.8

# Install Python 3 packages.
RUN conda install -c anaconda numpy=1.22.2
RUN conda install -c conda-forge matplotlib=3.5.1
RUN conda install -c anaconda pandas=1.4.1
RUN conda install -c anaconda pytest=6.2.5
RUN sudo apt-get install make=4.2.1


