# [complaint-management-system](https://complaint-management-demo.herokuapp.com/)

## Installation
- **Linux/Mac**
1. Open terminal using Ctrl+T. Run the following command <br>
`git clone https://github.com/khalidsaifullaah/complaint-management-system.git`

2. Create and active virtual environment using  <br>
` virtualenv -p python3 env` <br>
` cd env/Scripts` <br>
`activate.bat` <br>
3. Change the directory using <br>
`cd ..` <br>
` cd Complain_Management_System`<br>
4. Now you need to install python packages to run the app <br>
`pip3 install -r requirements.txt`
5. Migrations <br>
`python manage.py makemigrations`
`python manage.py migrate`
7. Run Django app <br>
`python manage.py runserver`
- **Windows**
1. Open terminal using WinKey+R then Type "cmd" and then click "OK" . Run the following command <br>
`git clone https://github.com/khalidsaifullaah/complaint-management-system.git`
2. Install and active virtual environment using  <br>
`pip install virtualenv` <br>
`virtualenv env` <br>
`env\Scripts\activate` <br>
3. Change the directory using <br>
` cd Complain_Management_System`<br>
4. Now you need to install python packages to run the app <br>
`pip3 install -r requirements.txt`
5. Migrations <br>
`python manage.py makemigrations`<br>
`python manage.py migrate --run-syncdb`
7. Run Django app <br>
`python manage.py runserver`
