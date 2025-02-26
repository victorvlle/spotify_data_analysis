from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType
from pyspark.sql.functions import explode

spark = SparkSession.builder.getOrCreate()

# schema = StructType([
#     StructField("items", ArrayType(StructType([
#         StructField("track", StructType([
#             StructField("album", StructType([
#                 StructField("album_type", StringType(), True)
#             ]), True)
#         ]), True)
#     ])), True)
# ])

df = spark.read.json(r"C:\Users\rvall\OneDrive\Área de Trabalho\victor\bd\spotify_data\extract\historico_spotify.json",multiLine = True)

df_exploded = df.select(explode("items").alias("item"))

df_tracks = df_exploded.select(
    "item.track.album.album_type",
    "item.track.name",
    explode("item.track.album.artists").alias("artist")                           
)

df_artists = df_tracks.select(
    "album_type",
    "name",
    "artist.name"
)

# df_artists.show(40,truncate=False)

df_cont = df_tracks.groupBy("artist.name").count()
df_cont.show(40,truncate=False)