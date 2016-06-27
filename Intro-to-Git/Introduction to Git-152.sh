## 1. Version control systems ##

~/random_numbers$ git init

## 2. The .git folder ##

~/random_numbers$ ls -al

## 3. Creating some files ##

~/random_numbers$ echo -e 'if __name__ == "__main__": /print("10")' >script.

## 4. Git status ##

~/random_numbers$ git add README.md

## 5. Configuring git ##

~/random_numbers$ git config --global user.name "George Varghese"

## 6. Committing ##

~/random_numbers$ git commit -m "Initial commit. Added script.py and README.md"

## 7. File differences ##

~/random_numbers$ git status

## 8. Making a second commit ##

~/random_numbers$ git commit

## 9. Looking at the commit history ##

~/random_numbers$ git log

## 10. Seeing commit differences ##

~/random_numbers$ git log --stat