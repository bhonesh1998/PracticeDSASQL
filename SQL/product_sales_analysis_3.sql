
select product_id,year as first_year ,quantity,price from (

select s.product_id,year,quantity,price,
rank() over ( partition by product_id order by year asc ) as rn
from Sales s
inner join
Product p
on
s.product_id = p.product_id
) der where rn=1


--spark sql


%scala
import org.apache.spark.sql.{SparkSession, DataFrame}
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.expressions.Window



val salesSchema = StructType(Seq(
  StructField("sale_id", IntegerType, false),
  StructField("product_id", IntegerType, false),
  StructField("year", IntegerType, false),
  StructField("quantity", IntegerType, false),
  StructField("price", IntegerType, false)
))

// Define schema for product DataFrame
val productSchema = StructType(Seq(
  StructField("product_id", IntegerType, false),
  StructField("product_name", StringType, false)
))

// Create sales DataFrame
val salesData = Seq(
  (1, 100, 2008, 10, 5000),
  (2, 100, 2009, 12, 5000),
  (7, 200, 2011, 15, 9000)
)

val salesDF = spark.createDataFrame(salesData).toDF("sale_id", "product_id", "year", "quantity", "price")

// Create product DataFrame
val productData = Seq(
  (100, "Nokia"),
  (200, "Apple"),
  (300, "Samsung")
)

val productDF = spark.createDataFrame(productData).toDF("product_id", "product_name")

val s = salesDF
val p = productDF

val win = Window.partitionBy("product_id").orderBy($"year")

val m = s.join(p,Seq("product_id"),"inner").withColumn("rn",rank().over(win))

m.filter($"rn"===1).show(10,false)

