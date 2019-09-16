# OnlineVoting
https://youtu.be/1Rge29HwGpo

    windows 7,8,10 etc

first download and install  python 3.0 and above framework on your computer 
  and confirm whether the python path has been configured by typing python on a command prompt

using cmd:
step..1 
install virtual environment 
 
   pip install virtualenv
   
step..2
creating & activating the virtual environment

   virtualenv <name>.(eg venv without the angle brackets)

   venv\scripts\activate (where 'venv' is my virtual environment )
   
step..3
install django

   pip install django==version(example: 2.2.1) 
step..4
install bootstrap3

   pip install django-bootstrap3
step..5
install pillow

   pip install pillow

(when using a proxy address)------pip install (package) -- proxy=https://user@mydomain:port)
   

to run server ,activate virtual environment then navigate to the project directory

 -------venv\scripts\activate
 
 -------(venv) C:\Project> cd OnlineVoting-Master
 
 --------------(venv) C:Project\OnlineVoting-Master>python manage.py runserver
