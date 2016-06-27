## 2. And operator ##

Select Major, ShareWomen, Employed from recent_grads where ShareWomen > 0.5 and Employed > 10000 Limit 10

## 3. Or operator ##

Select Major, Median, Unemployed from recent_grads where Median >= 10000 OR Unemployed <= 1000 Limit 20

## 4. Grouping operators ##

select Major, Major_category, ShareWomen, Unemployment_rate
from recent_grads
where (Major_category = 'Engineering') and (ShareWomen > 0.5 or Unemployment_rate < 0.051);

## 5. Practice grouping operators ##

Select Major, Major_category, Employed, Unemployment_rate from recent_grads where (Major_category = "Business" OR Major_category = "Arts" OR Major_category = "Health") and (Employed > 20000 OR Unemployment_rate < 0.051)

## 6. Order by ##

Select Major from recent_grads order by Major desc Limit 10

## 7. Order using multiple columns ##

Select Major_category, Median, Major from recent_grads order by Major asc, Median desc Limit 20