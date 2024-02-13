create virtual environment out sde of project
use venv command
```
> python -m venv venv
> venv/script/activate.ps1
```
now clone project
```
> git clone "url"
> cd "ethanpolls"
> pip install -r .\requirements.txt
```
add these varibles to a .env file
```sh
DJANGO_SECRETKEY="helloworld" 
DJANGO_DEBUG=True
> python manage.py migrate
```
create super user
```
> python manage.py createsuperuser
```
python .\manage.py runserver