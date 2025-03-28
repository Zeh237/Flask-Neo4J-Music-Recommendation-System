import pandas as pd
from sqlalchemy import text
from src.db_connection.mysqlDBConnection import DBConnection
from src.db_connection.neo4jDBConnection import Neo4jConnection


class Ingestion:
    def __init__(self):
        self.db_connection = DBConnection()
        self.engine = self.db_connection.create_db_connection()
        self.neo4j_connection = Neo4jConnection()

    def fetch_users(self):
        query = """
            SELECT id, name, country FROM users;
        """
        with self.engine.connect() as connection:
            result = pd.read_sql(text(query), connection)
        return result.to_dict(orient='records')

    def fetch_artists(self):
        query = """
            SELECT id, name, country FROM artists;
        """
        with self.engine.connect() as connection:
            result = pd.read_sql(text(query), connection)
        return result.to_dict(orient='records')

    def fetch_songs(self):
        query = """
            SELECT id, name, country, genre_id, created_at FROM songs;
        """
        with self.engine.connect() as connection:
            result = pd.read_sql(text(query), connection)
        return result.to_dict(orient='records')

    def fetch_genres(self):
        query = """
            SELECT id, name FROM genre;
        """
        with self.engine.connect() as connection:
            result = pd.read_sql(text(query), connection)
        return result.to_dict(orient='records')

    def fetch_song_artists(self):
        query = """
            SELECT song_id, artist_id FROM song_artists;
        """

        with self.engine.connect() as connection:
            result = pd.read_sql(text(query), connection)
        return result.to_dict(orient='records')

    def fetch_song_likes(self):
        query = """
            SELECT user_id, song_id from song_likes;
        """
        with self.engine.connect() as connection:
            result = pd.read_sql(text(query), connection)
        return result.to_dict(orient='records')

    def fetch_listen_logs(self):
        query = """
            SELECT user_id, song_id, count from listened_logs;
        """
        with self.engine.connect() as connection:
            result = pd.read_sql(text(query), connection)
        return result.to_dict(orient='records')

    def create_neo4j_schema(self):
        """Create constraints in Neo4j 4.1.13 compatible syntax"""
        schema_queries = [
            "CREATE CONSTRAINT ON (u:User) ASSERT u.id IS UNIQUE",
            "CREATE CONSTRAINT ON (a:Artist) ASSERT a.id IS UNIQUE",
            "CREATE CONSTRAINT ON (s:Song) ASSERT s.id IS UNIQUE",
            "CREATE CONSTRAINT ON (g:Genre) ASSERT g.id IS UNIQUE"
        ]

        for query in schema_queries:
            try:
                self.neo4j_connection.query(query)
            except Exception as e:
                return f"error: {e}"

    def load_users_to_neo4j(self):
        users = self.fetch_users()
        query = """
        UNWIND $users AS user
        MERGE (u:User {id: user.id})
        SET u.name = user.name,
            u.country = user.country
        """
        self.neo4j_connection.query(query, {"users": users})

    def load_artists_to_neo4j(self):
        artists = self.fetch_artists()
        query = """
        UNWIND $artists AS artist
        MERGE (a:Artist {id: artist.id})
        SET a.name = artist.name,
            a.country = artist.country
        """
        self.neo4j_connection.query(query, {"artists": artists})

    def load_genres_to_neo4j(self):
        genres = self.fetch_genres()
        query = """
        UNWIND $genres AS genre
        MERGE (g:Genre {id: genre.id})
        SET g.name = genre.name
        """
        self.neo4j_connection.query(query, {"genres": genres})

    def load_songs_to_neo4j(self):
        songs = self.fetch_songs()
        query = """
        UNWIND $songs AS song
        MERGE (s:Song {id: song.id})
        SET s.name = song.name,
            s.country = song.country,
            s.created_at = song.created_at
        WITH s, song
        MATCH (g:Genre {id: song.genre_id})
        MERGE (s)-[:BELONGS_TO]->(g)
        """
        self.neo4j_connection.query(query, {"songs": songs})

    def load_song_artists_to_neo4j(self):
        song_artists = self.fetch_song_artists()
        query = """
        UNWIND $song_artists AS sa
        MATCH (a:Artist {id: sa.artist_id})
        MATCH (s:Song {id: sa.song_id})
        MERGE (a)-[:PERFORMS]->(s)
        """
        self.neo4j_connection.query(query, {"song_artists": song_artists})

    def load_song_likes_to_neo4j(self):
        song_likes = self.fetch_song_likes()
        query = """
        UNWIND $song_likes AS sl
        MATCH (u:User {id: sl.user_id})
        MATCH (s:Song {id: sl.song_id})
        MERGE (u)-[:LIKES]->(s)
        """
        self.neo4j_connection.query(query, {"song_likes": song_likes})

    def load_listen_logs_to_neo4j(self):
        listen_logs = self.fetch_listen_logs()
        query = """
        UNWIND $listen_logs AS ll
        MATCH (u:User {id: ll.user_id})
        MATCH (s:Song {id: ll.song_id})
        MERGE (u)-[r:LISTENED]->(s)
        SET r.count = ll.count
        """
        self.neo4j_connection.query(query, {"listen_logs": listen_logs})

    def load_all_to_neo4j(self):
        try:
            self.create_neo4j_schema()
            self.load_genres_to_neo4j()
            self.load_artists_to_neo4j()
            self.load_users_to_neo4j()
            self.load_songs_to_neo4j()
            self.load_song_artists_to_neo4j()
            self.load_song_likes_to_neo4j()
            self.load_listen_logs_to_neo4j()
            return {"message": "database setup successfully"}
        except Exception as e:
            return {"message": f"{str(e)}"}

