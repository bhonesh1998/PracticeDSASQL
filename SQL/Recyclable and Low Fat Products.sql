# Write your MySQL query statement below
select product_id from Products
where low_fats='Y'
and recyclable='Y'


-- in spark sql

val df1 =
Seq(
(0,"Y","N"),
(1,"Y","Y"),
(2,"N","Y")
)
.toDF("product_id","low_fats","recyclable")

val df2 = df1.filter($"low_fats"==="Y" and $"recyclable"==="Y").select("product_id")

df2.show(4,false)