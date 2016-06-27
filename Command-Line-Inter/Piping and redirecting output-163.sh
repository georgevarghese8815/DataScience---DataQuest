## 1. Appending ##

~$ echo "Take one down, pass it around, 98 bottles of beer on the wall..." >> beer.tx

## 2. Redirecting from a file ##

~$ sort -r < beer.tx

## 3. The grep command ##

~$ grep "bottles of" beer.txt coffee.tx

## 4. Special characters ##

~$ grep "beer" beer?.tx

## 5. The star wildcard ##

~$ ls *.tx

## 6. Piping output ##

~$ python check.py | grep 27

## 7. Chaining commands ##

~$ echo "Whats up" >> beer.txt && cat beer.txt

## 8. Escaping characters ##

~$ echo "\"Whats up?\", asked I" >> beer.tx