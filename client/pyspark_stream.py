from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Set localhost socket parameters from ther server
HOST = "127.0.0.1"
PORT = 9090

# Create Spark session
spark = SparkSession.builder.appName("Twitter Stream Reader").getOrCreate()

# Create streaming DataFrame from local socket
# delimiter added on server side
stream = spark.readStream.format("socket") \
    .option("host", HOST) \
    .option("port", PORT) \
    .option("delimiter", "\n") \
    .load()

query = stream.writeStream.format("console") \
  .option("truncate", False) \
  .outputMode("append") \
  .start() \
  .awaitTermination()