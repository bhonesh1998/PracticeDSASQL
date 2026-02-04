select id from (
select id,
temperature,
lag(temperature) over (order by recordDate asc ) as pt,
lag(recordDate) over (order by recordDate asc ) as pre_dt,
recordDate as rt
from
Weather ) t where temperature-pt>0 and datediff(rt,pre_dt)=1