# Air Quality Dashboard

# Setup Environment - Anaconda
```
conda create --name air_quality_dashboard python=3.9
conda activate air_quality_dashboard
pip install -r requirements.txt
```
## Setup Environment - Shell/Terminal

```
mkdir air_quality_analysis
cd air_quality_analysis
pipenv install
pipenv shell
pip install -r requirements.txt
```


## Run steamlit app
```
streamlit run ".\dashboard\dashboard.py"
```
