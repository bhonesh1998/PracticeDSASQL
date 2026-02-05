# Write your MySQL query statement below

select tweet_id from Tweets
where
length(content)>15


val data = Seq(
  (1, "Let us Code"),
  (2, "More than fifteen chars are here!")
)

import org.apache.spark.sql.functions._

val df = data.toDF("id", "text")

val dfWithLength = df.withColumn("ll", length(col("text")))

dfWithLength.filter($"ll">15).show(1,false)

