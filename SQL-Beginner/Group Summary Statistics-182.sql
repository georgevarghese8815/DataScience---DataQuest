## 1. Statistics by group ##

Select * from recent_grads limit 5

## 2. The GROUP BY statement ##

SELECT Major_category, AVG(ShareWomen) FROM recent_grads GROUP BY Major_category;

## 3. The AS statement ##

Select Sum(Men) as total_men, sum(Women) as total_women from recent_grads

## 4. Practice: Using GROUP BY ##

SELECT Major_category, AVG(Employed) / AVG(Total) AS share_employed FROM recent_grads GROUP BY Major_category;

## 5. The HAVING statement ##

Select Major_category, AVG(Low_wage_jobs) / AVG(Total) as share_low_wage from recent_grads group by Major_category having share_low_wage > 0.1

## 6. The ROUND function ##

SELECT ROUND(ShareWomen, 4), Major_category FROM recent_grads LIMIT 10;

## 7. Nested functions ##

SELECT Major_category, ROUND(AVG(College_jobs) / AVG(Total), 3) AS share_degree_jobs FROM recent_grads GROUP BY Major_category HAVING share_degree_jobs < .3;