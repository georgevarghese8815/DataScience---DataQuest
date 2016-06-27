## 2. Calculating expected values ##

total = 32561
males_over50k = 0.241*0.669*total
males_under50k = 0.759 * 0.669 * total
females_over50k = 0.241 * 0.331 * total
females_under50k = 0.759 * 0.331 * total

## 3. Calculating chi-squared ##

mu50 = (15128 - 16533.5)**2/16533.5
mo50 = (6662 - 5249.8)**2/5429.8
fu50 = (9592 - 8180.3)**2/8180.3
fo50 = (1179 - 2597.4)**2/2597.4
chisq_gender_income = mu50 + mo50 + fu50 + fo50


#Alternate
observed = [6662, 1179, 15128, 9592]
expected = [5249.8, 2597.4, 16533.5, 8180.3]

values = []
for i, obs in enumerate(observed):
    exp = expected[i]
    sums = (obs - exp)**2/exp
    values.append(sums)

chisq_gender_income = sum(values)

## 4. Finding statistical significance ##

from scipy.stats import chisquare
chisquare_gender_income, pvalue_gender_income = chisquare(observed, expected)

## 5. Cross tables ##

from pandas import crosstab
crosstab(income["sex"], [income["race"]])

## 6. Finding expected values ##

from scipy.stats import chi2_contingency
chisq_value, pvalue_gender_race, df, expected = chi2_contingency(table)