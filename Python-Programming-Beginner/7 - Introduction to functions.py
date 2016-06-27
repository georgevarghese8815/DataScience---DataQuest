## 1. Overview ##

a = open("dictionary.txt", "r")
vocabulary = a.read()
print(vocabulary)

## 2. Tokenizing the vocabulary ##

vocabulary = open("dictionary.txt", "r").read()
tokenized_vocabulary = vocabulary.split(' ')
tokenized_vocabulary[0:5]

## 3. Replacing special characters ##

f = open("story.txt", 'r')
story_string = f.read()

print(story_string)
story_string = story_string.replace(".","")
story_string = story_string.replace(",","")
story_string = story_string.replace("'", "")
story_string = story_string.replace(";", "")
story_string = story_string.replace("\n", "")
print(story_string)

## 5. Practice: Creating a function to clean text ##

f = open("story.txt", 'r')
story_string = f.read()

def clean_text(text_string):
    cleaned_string = text_string.replace(".","")
    cleaned_string = cleaned_string.replace("'","")
    cleaned_string = cleaned_string.replace(";","")
    cleaned_string = cleaned_string.replace(",","")
    cleaned_string = cleaned_string.replace("\n","")
    return cleaned_string

cleaned_story = clean_text(story_string)
print(story_string)
print(cleaned_story)

## 6. Lowercasing the words ##

def clean_text(text_string):
    cleaned_string = text_string.replace(",","")
    cleaned_string = cleaned_string.replace(".","")
    cleaned_string = cleaned_string.replace("'", "")
    cleaned_string = cleaned_string.replace(";", "")
    cleaned_string = cleaned_string.replace("\n", "")
    return(cleaned_string.lower())
cleaned_story = clean_text(story_string)

## 7. Multiple arguments ##

f = open("story.txt", 'r')
story_string = f.read()
clean_chars = [",", ".", "'", ";", "\n"]

# Previous code for clean_text().
def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for item in special_characters:
        cleaned_string = cleaned_string.replace(item, "")
    cleaned_string = cleaned_string.lower() 
    return(cleaned_string)

cleaned_story = clean_text(story_string, clean_chars)
print(cleaned_story)

## 8. Tokenizing the story ##

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

clean_chars = [",", ".", "'", ";", "\n"]

def tokenize(text_string, special_characters):
    cleaned_story = clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)
    
tokenized_story = tokenize(story_string, clean_chars)
print(tokenized_story)

## 9. Finding misspelled words ##

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters):
    cleaned_story = clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)

misspelled_words = []
clean_chars = [",", ".", "'", ";", "\n"]
tokenized_story = tokenize(story_string, clean_chars)
tokenized_vocabulary = tokenize(vocabulary, clean_chars)
misspelled_words = []
for item in tokenized_story:
    if item not in tokenized_vocabulary:
        misspelled_words.append(item)
print(misspelled_words)