from flask import Flask, jsonify, request, abort, make_response, Response, Blueprint
from src.services.RecommendationService import RecommendationService
from src.services.DataIngestionService import Ingestion

api = Blueprint('api', __name__)
recommendationService = RecommendationService()
ingestionService = Ingestion()

@api.route("/", methods=["GET"])
def hello():
    return "Hello world"

# recommend based on users listening activities
@api.route("/user_activity_recommendations", methods=["POST"])
def user_activity():
    data = request.get_json()
    user_id = data.get("user_id")
    limit = data.get("limit", 20)
    page = data.get("page", 1)
    if not data.get("user_id"):
        return make_response(jsonify({"error": "user_id required"}), 400)

    response = recommendationService.recommend_based_on_user_activity(user_id, limit, page)
    return make_response(jsonify(response), 200)

# recommend based on artists listened to by user
@api.route("/user_artist_recommendations", methods=["POST"])
def user_artist():
    data = request.get_json()
    user_id = data.get("user_id")
    limit = data.get("limit", 20)
    page = data.get("page", 1)
    if not data.get("user_id"):
        return make_response(jsonify({"error": "user_id required"}), 400)

    response = recommendationService.recommend_based_on_artists(user_id, limit, page)
    return make_response(jsonify(response), 200)

# recommend based on genre listened to by user
@api.route("/user_genre_recommendations", methods=["POST"])
def user_genre():
    data = request.get_json()
    user_id = data.get("user_id")
    limit = data.get("limit", 20)
    page = data.get("page", 1)
    if not data.get("user_id"):
        return make_response(jsonify({"error": "user_id required"}), 400)

    response = recommendationService.recommend_based_on_genre(user_id, limit, page)
    return make_response(jsonify(response), 200)

# recent songs the user might have interest in
@api.route("/user_recent_songs_recommendations", methods=["POST"])
def user_recent_songs():
    data = request.get_json()
    user_id = data.get("user_id")
    limit = data.get("limit", 20)
    page = data.get("page", 1)
    if not data.get("user_id"):
        return make_response(jsonify({"error": "user_id required"}), 400)

    response = recommendationService.get_recently_added_songs(user_id, limit, page)
    return make_response(jsonify(response), 200)

# setup database
@api.route("/setup", methods=["POST"])
def setup():
    response = ingestionService.load_all_to_neo4j()
    return make_response(jsonify(response), 200)
