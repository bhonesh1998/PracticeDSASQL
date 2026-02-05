


# Write your MySQL query statement below
select name from
Customer
where  (referee_id !=2) or referee_id is null







-- spark sql



val data = Seq( (1, "Will", null), (2, "Jane", null), (3, "Alex", Some(2)), (4, "Bill", null), (5, "Zack", Some(1)), (6, "Mark", Some(2))
).toDF("id","name","rid")

data.filter(($"rid"=!=2) or $"rid".isNull).show(10,false)

