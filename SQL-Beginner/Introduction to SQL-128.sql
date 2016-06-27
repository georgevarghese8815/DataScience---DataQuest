## 4. SQLite ##

Select Rank, Major from recent_grads;

## 5. Specifying column order ##

Select Major, Rank from recent_grads

## 6. Practice: Select ##

Select Rank, Major_code, Major, Major_category, Total from recent_grads

## 7. Where ##

Select Major, ShareWomen from recent_grads where ShareWomen > 0.5

## 8. Practice: Where ##

Select Major, Employed from recent_grads where Employed > 10000

## 9. Limit ##

Select Major from recent_grads where Employed > 10000 LIMIT 10