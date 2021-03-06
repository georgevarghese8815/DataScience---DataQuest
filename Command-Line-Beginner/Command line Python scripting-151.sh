## 1. Command line Python ##

~$ python script.py echo -e 'if __name__ == "__main__":\n print("Welcome to a Python script")' > script.py

## 2. Python versions ##

~$ python3 script.py

## 3. Installing packages ##

~$ pip install requests

## 4. Virtual environments ##

~$ virtualenv python2

## 5. Python 3 virtualenv ##

~$ virtualenv -p /usr/bin/python3 python3

## 6. Activating a virtualenv ##

~$ source python3/bin/activate

## 7. Checking the installed packages ##

(python3) ~$ pip freeze

## 8. Importing a file ##

(python3) ~$ python script.py echo -e 'def print_message():\n print("Hello from another file!")' > ut ils.py

## 9. Command line arguments ##

(python3) ~$ python script.py "Hello from the command line"

## 10. Deactivating a virtualenv ##

~$ deactivate