from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("items", ArrayType(StructType([
        StructField("track", StructType([
            StructField("album", StructType([
                StructField("album_type", StringType(), True)
            ]), True)
        ]), True)
    ])), True)
])

df = spark.read.schema(schema).json(r"C:\Users\rvall\OneDrive\Área de Trabalho\victor\bd\spotify_data\extract\historico_spotify.json")

df.show(truncate = False)

