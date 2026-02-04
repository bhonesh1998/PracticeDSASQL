# Write your MySQL query statement below

select
customer_id ,
sum(case when transaction_id is null then 1 else 0 end ) as count_no_trans
from (
select customer_id,transaction_id
from Visits v
left join
Transactions t
on v.visit_id = t.visit_id
) jt
group by customer_id having count_no_trans>0
