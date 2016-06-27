## 1. Introduction ##

raw_hamlet = sc.textFile("hamlet.txt")

## 2. Map ##

split_hamlet = raw_hamlet.map(lambda line: line.split('\t'))
split_hamlet.take(3)

## 3. Beyond lambda functions ##

def hamlet_speaks(line):
    id = line[0]
    speaketh = False
    
    if "HAMLET" in line:
        speaketh = True
    
    if speaketh:
        yield id,"hamlet speaketh!"

hamlet_spoken = split_hamlet.flatMap(lambda x: hamlet_speaks(x))
hamlet_spoken.take(10)

## 4. Filter() using a named function ##

def filter_hamlet_speaks(line):
    if "HAMLET" in line:
        return True
    else:
        return False

hamlet_spoken_lines = split_hamlet.filter(lambda line: filter_hamlet_speaks(line))
hamlet_spoken_lines.take(5)

## 5. Actions ##

spoken_count = 0
spoken_101 = list()
spoken_count = hamlet_spoken_lines.count()
spoken_collect = hamlet_spoken_lines.collect()
spoken_101 = spoken_collect[100]