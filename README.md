
python -m venv onlyflan_env
onlyflan_env\Scripts\activate  
pip install -r requirements.txt 
cd onlyflan
python manage.py makemigrations  
python manage.py migrate  
python manage.py seed
python manage.py runserver


![Logo del Proyecto](brownie.jpg)