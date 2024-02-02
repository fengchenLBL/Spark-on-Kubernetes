# hello_world.py
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("HelloWorld").getOrCreate()
    sc = spark.sparkContext

    rdd = sc.parallelize([1, 2, 3, 4, 5])
    rdd.foreach(print)

    spark.stop()
