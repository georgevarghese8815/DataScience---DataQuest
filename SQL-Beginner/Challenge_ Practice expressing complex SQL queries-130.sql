## 2. Select and Limit ##

Select College_jobs, Median, Unemployment_rate from recent_grads Limit 20

## 3. Where ##

Select Major from recent_grads where Major_category = "Arts" limit 5

## 4. Operators ##

Select Major, Total, Median, Unemployment_rate from recent_grads where (Major_category != 'Engineering') AND (Median <= 50000 or Unemployment_rate > 0.065)

## 5. Ordering ##

Select Major from recent_grads where Major_category != 'Engineering' order by Major desc limit 20