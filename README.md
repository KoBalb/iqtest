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



# Api endpoints
1.http://127.0.0.1:8000/api/questions/
[
    {
        "id": 2,
        "image_src": "http://127.0.0.1:8000/media/questions/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-03-10_154922_O82xSBf.png",
        "correct_option": 1,
        "score": 20,
        "option_1": "http://127.0.0.1:8000/media/options/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-02-18_145329_uivyQoZ.png",
        "option_2": "http://127.0.0.1:8000/media/options/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-02-07_164631_8Ry1fEM.png",
        "option_3": "http://127.0.0.1:8000/media/options/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-03-20_032555_kQOh7WQ.png",
        "option_4": "http://127.0.0.1:8000/media/options/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-03-18_141919_JQ8usIm.png"
    },
    {
        "id": 3,
        "image_src": "http://127.0.0.1:8000/media/questions/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-04-04_230059.png",
        "correct_option": 2,
        "score": 10,
        "option_1": "http://127.0.0.1:8000/media/options/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-04-03_153616.png",
        "option_2": "http://127.0.0.1:8000/media/options/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-04-03_145417.png",
        "option_3": "http://127.0.0.1:8000/media/options/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-03-25_123047.png",
        "option_4": "http://127.0.0.1:8000/media/options/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-03-10_180845.png"
    }
]

2.http://127.0.0.1:8000/api/result/
Example
{
  "gender": "F",
  "age": "2",
  "email": "artem.kovalyk79@gmail.com",
  "score": "1123111",
  "time_test": 1
}