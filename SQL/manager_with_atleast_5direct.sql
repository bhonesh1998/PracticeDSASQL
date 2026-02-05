# Write your MySQL query statement below



select name from Employee where id in  (
select managerId
from
Employee
group by managerId
having count(managerId)>=5
)


%scala
val data = Seq(
  (101, "John", "A", None),  // Use None for NULL values
  (102, "Dan", "A", Some(101)),
  (103, "James", "A", Some(101)),
  (104, "Amy", "A", Some(101)),
  (105, "Anne", "A", Some(101)),
  (106, "Ron", "B", Some(101))
)
import org.apache.spark.sql.functions._


// Convert to DataFrame
val df = data.toDF("id", "name", "department", "manager_id")

val df1 = df.groupBy("manager_id").agg(count($"manager_id").as("c")).filter($"c">=5)
.select("manager_id").collect.map(_.getAs[Int]("manager_id")).toSeq



val df2 = df.select("name","id").filter($"id".isin(df1: _*))


df2.show(2,false)


