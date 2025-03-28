from math import ceil

from src.db_connection.mysqlDBConnection import DBConnection
from src.db_connection.neo4jDBConnection import Neo4jConnection


class RecommendationService:
    def __init__(self):
        self.db_connection = DBConnection()
        self.engine = self.db_connection.create_db_connection()
        self.neo4j_connection = Neo4jConnection()

    def recommend_based_on_user_activity(self, user_id, limit=20, page=1):

        count_query = """
                MATCH (u:User {id: $user_id})-[:LISTENED|LIKES]->()<-[:LISTENED|LIKES]-(other:User)
                MATCH (other)-[:LISTENED|LIKES]->(rec:Song)
                WHERE NOT EXISTS((u)-[:LISTENED|LIKES]->(rec))
                RETURN count(DISTINCT rec) AS total_count
                """
        count_result = self.neo4j_connection.query(count_query, {"user_id": user_id})
        total_items = count_result[0]['total_count'] if count_result else 0
        total_pages = ceil(total_items / limit) if total_items > 0 else 1

        page = max(1, min(page, total_pages))
        offset = (page - 1) * limit

        query = """
                MATCH (u:User {id: $user_id})-[:LISTENED|LIKES]->()<-[:LISTENED|LIKES]-(other:User)
                MATCH (other)-[:LISTENED|LIKES]->(rec:Song)
                WHERE NOT EXISTS((u)-[:LISTENED|LIKES]->(rec))
                WITH rec, count(other) AS common_activities
                RETURN rec.id AS song_id,
                       rec.name AS song_name,
                       common_activities AS activity_score,
                       [(a)-[:PERFORMS]->(rec) | a.name][..3] AS artists,
                       [(other)-[:LISTENED|LIKES]->(rec) | other.id][..5] AS similar_users
                ORDER BY activity_score DESC
                SKIP $offset
                LIMIT $limit
                """
        params = {
            "user_id": user_id,
            "offset": offset,
            "limit": limit
        }

        recommendations = self.neo4j_connection.query(query, params)

        return {
            "recommendations": recommendations,
            "total_items": total_items,
            "total_pages": total_pages,
            "current_page": page,
            "per_page": limit
        }

    def recommend_based_on_artists(self, user_id, limit=20, page=1):

        count_query = """
            MATCH (u:User {id: $user_id})-[:LISTENED|LIKES]->(s:Song)<-[:PERFORMS]-(a:Artist)
            MATCH (a)-[:PERFORMS]->(rec:Song)
            WHERE NOT EXISTS((u)-[:LISTENED|LIKES]->(rec))
            RETURN count(DISTINCT rec) AS total_count
            """
        count_result = self.neo4j_connection.query(count_query, {"user_id": user_id})
        total_items = count_result[0]['total_count'] if count_result else 0
        total_pages = ceil(total_items / limit) if total_items > 0 else 1

        page = max(1, min(page, total_pages))
        offset = (page - 1) * limit

        query = """
            MATCH (u:User {id: $user_id})-[:LISTENED|LIKES]->(s:Song)<-[:PERFORMS]-(a:Artist)
            MATCH (a)-[:PERFORMS]->(rec:Song)
            WHERE NOT EXISTS((u)-[:LISTENED|LIKES]->(rec))
            WITH rec, a, count(*) AS artist_affinity
            RETURN rec.id AS song_id,
                   rec.name AS song_name,
                   a.name AS artist_name,
                   artist_affinity,
                   [(a2)-[:PERFORMS]->(rec) WHERE a2 <> a | a2.name][..2] AS other_artists
            ORDER BY artist_affinity DESC
            SKIP $offset
            LIMIT $limit
            """
        params = {
            "user_id": user_id,
            "offset": offset,
            "limit": limit
        }

        recommendations = self.neo4j_connection.query(query, params)

        return {
            "recommendations": recommendations,
            "total_items": total_items,
            "total_pages": total_pages,
            "current_page": page,
            "per_page": limit
        }

    def recommend_based_on_genre(self, user_id, limit=20, page=1):

        count_query = """
            MATCH (u:User {id: $user_id})-[:LISTENED|LIKES]->(s:Song)-[:BELONGS_TO]->(g:Genre)
            MATCH (g)<-[:BELONGS_TO]-(rec:Song)
            WHERE NOT EXISTS((u)-[:LISTENED|LIKES]->(rec))
            RETURN count(DISTINCT rec) AS total_count
            """
        count_result = self.neo4j_connection.query(count_query, {"user_id": user_id})
        total_items = count_result[0]['total_count'] if count_result else 0
        total_pages = ceil(total_items / limit) if total_items > 0 else 1

        # Adjust page if out of range
        page = max(1, min(page, total_pages))
        offset = (page - 1) * limit

        # Get paginated recommendations with genre affinity
        query = """
            MATCH (u:User {id: $user_id})-[:LISTENED|LIKES]->(s:Song)-[:BELONGS_TO]->(g:Genre)
            MATCH (g)<-[:BELONGS_TO]-(rec:Song)
            WHERE NOT EXISTS((u)-[:LISTENED|LIKES]->(rec))
            WITH rec, g, count(*) AS genre_affinity
            RETURN rec.id AS song_id,
                   rec.name AS song_name,
                   g.name AS genre,
                   genre_affinity,
                   [(a)-[:PERFORMS]->(rec) | a.name][..3] AS artists
            ORDER BY genre_affinity DESC
            SKIP $offset
            LIMIT $limit
            """
        params = {
            "user_id": user_id,
            "offset": offset,
            "limit": limit
        }

        recommendations = self.neo4j_connection.query(query, params)

        return {
            "recommendations": recommendations,
            "total_items": total_items,
            "total_pages": total_pages,
            "current_page": page,
            "per_page": limit
        }

    def get_recently_added_songs(self, user_id, limit=20, page=1):

        count_query = """
            MATCH (s:Song)
            WHERE NOT EXISTS((:User {id: $user_id})-[:LISTENED|LIKES]->(s))
            RETURN count(s) AS total_count
            """
        count_result = self.neo4j_connection.query(count_query, {"user_id": user_id})
        total_items = count_result[0]['total_count'] if count_result else 0
        total_pages = ceil(total_items / limit) if total_items > 0 else 1

        # Adjust page if out of range
        page = max(1, min(page, total_pages))
        offset = (page - 1) * limit

        # Get paginated recent songs with additional metadata
        query = """
            MATCH (s:Song)
            WHERE NOT EXISTS((:User {id: $user_id})-[:LISTENED|LIKES]->(s))
            OPTIONAL MATCH (s)-[:BELONGS_TO]->(g:Genre)
            OPTIONAL MATCH (a)-[:PERFORMS]->(s)
            WITH s, g, collect(DISTINCT a.name)[..3] AS artists
            RETURN s.id AS song_id,
                   s.name AS song_name,
                   artists,
                   g.name AS genre,
                   s.created_at AS release_date,
                   date().epochSeconds - datetime(s.created_at).epochSeconds <= 2592000 AS is_new_release
            ORDER BY s.created_at DESC
            SKIP $offset
            LIMIT $limit
            """
        params = {
            "user_id": user_id,
            "offset": offset,
            "limit": limit
        }

        recommendations = self.neo4j_connection.query(query, params)

        return {
            "recommendations": recommendations,
            "total_items": total_items,
            "total_pages": total_pages,
            "current_page": page,
            "per_page": limit
        }
