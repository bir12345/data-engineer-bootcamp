from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


if __name__ == "__main__":
    spark = SparkSession.builder.appName("CarPowerTransformation").getOrCreate()

def transform_car_data(spark):
    data = [
        ("Ford Torino", 140, 3449, "US"),
        ("Chevrolet Monte Carlo", 150, 3761, "US"),
        ("BMW 2002", 113, 2234, "Europe"),
    ]

    schema = StructType([
        StructField("carr", StringType(), True),
        StructField("horsepower", IntegerType(), True),
        StructField("weight", IntegerType(), True),
        StructField("origin", StringType(), True),
    ])

    df = spark.createDataFrame(data=data, schema=schema)
    df.printSchema()
    df.show()
