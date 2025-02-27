from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType
from pyspark.sql.functions import explode, col, expr

spark = SparkSession.builder.getOrCreate()

df = spark.read.json(r"C:\Users\rvall\OneDrive\Área de Trabalho\victor\bd\spotify_data\spotify_tracks.json",multiLine = True)

df_itens = df.select(
    explode("`Melhores Sertanejos 2025 🔝 `.items").alias("item")
)

df_musicas = df_itens.select(
    col("item.added_at").alias("added_date"),
    col("item.track.explicit").alias("explicit"),
    col("item.track.album.id").alias("album_id"),
    col("item.track.album.name").alias("album_name"),
    col("item.track.album.release_date").alias("album_release_date"),
    explode("item.track.album.artists").alias("artist"),
    col("item.track.duration_ms").alias("track_duration"),
    col("item.track.id").alias("track_id"),
    col("item.track.name").alias("track_name"),
    col("item.track.popularity").alias("track_popularity"),
)

df_geral = df_musicas.select(
    "track_id",
    "track_name",
    col("artist.id").alias("artist_id"),
    col("artist.name").alias("artist_name"),
    "track_duration",
    "album_id",
    "album_name",
    "album_release_date",
    "track_popularity",
)

df_artistas = df_geral.select(
    "artist_id",
    "artist_name"
).groupBy("artist_name").count().orderBy(col("count").desc())

df_geral.show(100)