## 2. Adding columns ##

Alter table facts
Add leader text

## 6. Creating a table with relations ##

Create table factbook.states(
    id integer PRIMARY KEY,
    name text,
    area integer,
    country integer,
    Foreign Key(country) references facts(id)
);


## 7. Querying across foreign keys ##

Select * from landmarks
inner join facts
on landmarks.country = facts.id

## 8. Types of joins ##

Select * from landmarks
left outer join facts
on landmarks.country = facts.id