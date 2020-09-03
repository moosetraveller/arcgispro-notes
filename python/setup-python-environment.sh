# Get Anaconda if not yet installed
# wget https://repo.anaconda.com/archive/Anaconda3-2019.10-MacOSX-x86_64.sh
# sh Anaconda3-2019.10-MacOSX-x86_64.sh

# Create a fresh environment with python 3.7
conda create --name autogis python=3.7 geopandas --yes

# Activate the environment
conda activate gis

# Install packages
conda install -y jupyterlab matplotlib geojson mapclassify contextily folium mplleaflet osmnx

# Start jupyter lab
jupyter lab
