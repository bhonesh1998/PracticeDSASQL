# Write your MySQL query statement below

# Write your MySQL query statement below

select user_id,
round(avg(if(action='confirmed',1,0)),2) as confirmation_rate
from
( select s.user_id , e.action
from Signups s
left join
(
select user_id,action from Confirmations
)e
 on s.user_id = e.user_id
) f
group by user_id


