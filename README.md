# iqtest

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Go to project folder
cd iqtest
# Install frameworks
pip install -r requirements.txt

# Make migration
python manage.py migrate  

# Run project
python manage.py runserver

# Create admin ? if necessary
python manage.py createsuperuser
