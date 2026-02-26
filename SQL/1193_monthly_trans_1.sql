
--https://leetcode.com/problems/monthly-transactions-i/

select month1 as month , country ,
count(id) as trans_count,
sum(case when a_fla = 1 then 1 else 0 end) as approved_count,
sum(amount) as trans_total_amount,
sum(case when a_fla = 1 then amount else 0 end) as approved_total_amount
from
(select *, concat(year(trans_date),"-",date_format(trans_date,"%m")) as month1, case when state='approved' then 1 else 0 end as a_fla
from Transactions
)t
group by month1,country