from flask import request, jsonify
from bson import ObjectId
import cloudinary.uploader
import logging
from models import Post, Comment
from extensions import posts_collection, comments_collection

def get_posts():
    try:
        posts = list(posts_collection.find().sort("created_at", -1))
        for post in posts:
            post['_id'] = str(post['_id'])

            comments = list(comments_collection.find({"post_id": ObjectId(post['_id'])}))
            for comment in comments:
                comment['_id'] = str(comment['_id'])
                comment['post_id'] = str(comment['post_id'])
                comment['user_username'] = str(comment['user_username'])
            post['comments'] = comments

        return jsonify(posts), 200
    except Exception as e:
        logging.error(f"Error retrieving posts: {str(e)}")
        return jsonify({"error": "Failed to retrieve posts"}), 500

def upload_image_to_cloudinary(image):
    try:
        upload_result = cloudinary.uploader.upload(image, folder="Devhub/Posts")
        return upload_result['secure_url']
    except Exception as e:
        logging.error(f"Error uploading image: {str(e)}")
        return None

def create_post():
    try:
        data = request.form
        author_username = data.get('author_username')
        description = data.get('description')
        tags = data.getlist('tags')
        
        if not author_username or not description:
            return jsonify({'error': 'Author username and description are required'}), 400

        image_url = None
        if 'image' in request.files:
            image_file = request.files['image']
            if image_file.filename != '':
                image_url = upload_image_to_cloudinary(image_file)
                if image_url is None:
                    return jsonify({'error': 'Image upload failed'}), 500

        post = Post.create_post(author_username, description, tags, image_url)
        return jsonify({"post_id": str(post.inserted_id)}), 201
    except Exception as e:
        logging.error(f"Error creating post: {str(e)}")
        return jsonify({"error": "Failed to create post"}), 500

def update_post(post_id):
    try:
        data = request.get_json()
        description = data.get('description')
        tags = data.get('tags')
        image_link = data.get('image_link')

        if not description and not tags and not image_link:
            return jsonify({"error": "Nothing to update"}), 400

        success = Post.update_post(post_id, description, tags, image_link)
        if not success:
            return jsonify({"error": "Post not found"}), 404

        return jsonify({"message": "Post updated"}), 200
    except Exception as e:
        logging.error(f"Error updating post: {str(e)}")
        return jsonify({"error": "Failed to update post"}), 500

def delete_post(post_id):
    try:
        success = Post.delete_post(post_id)
        if not success:
            return jsonify({"error": "Post not found"}), 404
        return jsonify({"message": "Post deleted"}), 200
    except Exception as e:
        logging.error(f"Error deleting post: {str(e)}")
        return jsonify({"error": "Failed to delete post"}), 500

def vote_post(post_id, vote_type):
    if vote_type not in ['upvote', 'downvote']:
        return jsonify({"error": "Invalid vote type"}), 400
    try:
        success = Post.vote_post(post_id, vote_type)
        if not success:
            return jsonify({"error": "Post not found"}), 404
        return jsonify({"message": f"Post {vote_type}d"}), 200
    except Exception as e:
        logging.error(f"Error voting on post: {str(e)}")
        return jsonify({"error": f"Failed to {vote_type} post"}), 500

def add_comment(post_id):
    try:
        data = request.get_json()
        user_username = data.get('user_username')
        text = data.get('text')

        if not user_username or not text:
            return jsonify({'error': 'Username and comment text are required'}), 400

        comment = Comment.add_comment(post_id, user_username, text)
        if not comment:
            return jsonify({"error": "Failed to add comment"}), 500

        return jsonify({"comment_id": str(comment.inserted_id)}), 201
    except Exception as e:
        logging.error(f"Error adding comment: {str(e)}")
        return jsonify({"error": "Failed to add comment"}), 500

def delete_comment(comment_id):
    try:
        success = Comment.delete_comment(comment_id)
        if not success:
            return jsonify({"error": "Comment not found"}), 404
        return jsonify({"message": "Comment deleted"}), 200
    except Exception as e:
        logging.error(f"Error deleting comment: {str(e)}")
        return jsonify({"error": "Failed to delete comment"}), 500
