# hello_world.py
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("HelloWorld").getOrCreate()
    sc = spark.sparkContext

    data = ["Hello", "World"]
    rdd = sc.parallelize(data)
    rdd.foreach(print)

    spark.stop()
