## 4. Querying a normalized database ##

cursor = conn.cursor()
query = "Select ceremonies.year, nominations.movie from nominations inner join ceremonies on nominations.ceremony_id = ceremonies.id where nominee = \"Natalie Portman\" "
cursor.execute(query)
portman_movies = cursor.fetchall()
print(portman_movies)

## 6. Join table ##

cursor = conn.cursor()
query1 = '''Select * from movies_actors limit 5'''
query2 = '''Select * from actors limit 5'''
query3 = '''Select * from movies limit 5'''
five_join_table = cursor.execute(query1).fetchall()
five_actors = cursor.execute(query2).fetchall()
five_movies = cursor.execute(query3).fetchall()

## 7. Querying a many-to-many relation ##

query = '''SELECT actors.actor, movies.movie FROM movies
INNER JOIN movies_actors ON movies.id == movies_actors.movie_id
INNER JOIN actors ON movies_actors.actor_id == actors.id
WHERE movies.movie == "The King's Speech";'''
kings_actors = conn.execute(query).fetchall()
print(kings_actors)

## 8. Practice: querying a many-to-many relation ##

query = '''Select movies.movie, actors.actor from movies 
inner join movies_actors on movies.id = movies_actors.movie_id
inner join actors on movies_actors.actor_id = actors.id
where actors.actor = "Natalie Portman"'''
portman_joins = conn.execute(query).fetchall()
print(portman_joins)