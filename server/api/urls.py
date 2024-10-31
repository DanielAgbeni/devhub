from api.handlers.auth.userauth import signup, login, check_auth, home, logout, index, check_username
from api.handlers.user.profile import get_profile, update_profile
from api.handlers.projects.projects import add_project, update_project, delete_project, get_projects, increment_star, project_details, upload_image
from api.handlers.analyze.githubdata import github_data, top_languages, streak_stats, pinned_repos, streak_chart
from api.handlers.analyze.leetcodedata import leetcode_data, leetcode_card
from api.handlers.query.querymodel import chat,chat_history
from api.handlers.user.friends import add_friend, remove_friend, get_friends
from api.handlers.message.message import search_users, send_message, get_messages, get_chatted_users, get_chat_history
from api.handlers.visualization.visualization import get_user_relations
from api.handlers.neo4jconnect.connect import connect_to_neo4j, execute_cypher, schema
from api.handlers.posts.posts import create_post, update_post, delete_post, vote_post, add_comment, delete_comment, get_posts, get_posts_by_author, get_post_by_id
from api.handlers.suggestions.usersuggestions import get_user_suggestions

def register_routes(app):
    # Authentication routes
    app.add_url_rule('/signup', 'signup', signup, methods=['POST'])
    app.add_url_rule('/check_username', 'check_username', check_username, methods=['GET'])
    app.add_url_rule('/login', 'login', login, methods=['POST'])
    app.add_url_rule('/check_auth', 'check_auth', check_auth, methods=['GET'])
    app.add_url_rule('/logout', 'logout', logout)
    
    # Home route
    app.add_url_rule('/home', 'home', home)
    
    # Profile routes
    app.add_url_rule('/profile/<username>', 'get_profile', get_profile, methods=['GET'])
    app.add_url_rule('/profile/<username>', 'update_profile', update_profile, methods=['PUT'])
    
    # Friends routes
    app.add_url_rule('/profile/<username>/friends','add_friend',add_friend, methods=['POST'])
    app.add_url_rule('/profile/<username>/friends','remove_friend',remove_friend, methods=['DELETE'])
    app.add_url_rule('/profile/<username>/friends','get_friends',get_friends, methods=['GET'])
    
    # Analyze routes - Github
    app.add_url_rule('/analyze/github_data', 'github_data', github_data, methods=['POST'])
    app.add_url_rule('/analyze/top_languages', 'top_languages', top_languages, methods=['POST'])
    app.add_url_rule('/analyze/streak_stats', 'streak_stats', streak_stats, methods=['POST'])
    app.add_url_rule('/analyze/pinned_repos', 'pinned_repos', pinned_repos, methods=['POST'])
    app.add_url_rule('/analyze/streak_chart', 'streak_chart', streak_chart, methods=['POST'])
    
    # Analyze routes - Leetcode
    app.add_url_rule('/analyze/leetcode_data', 'leetcode_data', leetcode_data, methods=['POST'])
    app.add_url_rule('/analyze/leetcode_card', 'leetcode_card', leetcode_card, methods=['POST'])
    
    # Project routes
    app.add_url_rule('/profile/<username>/projects', 'get_projects', get_projects, methods=['GET'])
    app.add_url_rule('/profile/<username>/projects', 'add_project', add_project, methods=['POST'])
    app.add_url_rule('/profile/<string:username>/projects/<string:project_id>', 'project_details', project_details, methods=['GET'])
    app.add_url_rule('/profile/<string:username>/projects/<string:project_id>', 'update_project', update_project, methods=['PUT'])
    app.add_url_rule('/profile/<username>/projects/<string:project_id>', 'delete_project', delete_project, methods=['DELETE'])
    app.add_url_rule('/profile/<username>/projects/<project_id>/star', 'increment_star', increment_star, methods=['POST'])
    app.add_url_rule('/project/upload', 'upload_image', upload_image, methods=['POST'])
    
    # Chat with model routes
    app.add_url_rule('/chat', 'chat', chat, methods=['POST'])
    app.add_url_rule('/chat_history', 'chat_history', chat_history, methods=['GET'])
    
    # Messaging routes
    app.add_url_rule('/search_users', 'search_users', search_users, methods=['GET'])
    app.add_url_rule('/send', 'send_message', send_message, methods=['POST']) 
    app.add_url_rule('/messages', 'get_messages', get_messages, methods=['GET'])
    app.add_url_rule('/chatted_users/<username>', 'get_chatted_users', get_chatted_users, methods=['GET'])
    app.add_url_rule('/chat_history/<user1>/<user2>','get_chat_history',get_chat_history, methods=['GET'])
    
    # Visualization route
    app.add_url_rule('/profile/relations','get_user_relations',get_user_relations, methods=['GET'])
    
    # New Neo4j Connection route
    app.add_url_rule('/new-connection','connect_to_neo4j',connect_to_neo4j,methods=['POST'])
    app.add_url_rule('/execute-cypher','execute_cypher',execute_cypher,methods=['POST'])
    app.add_url_rule('/db-schema', 'schema', schema, methods=['POST'])
    
    # Posts routes
    app.add_url_rule('/posts', 'get_posts', get_posts, methods=['GET'])
    app.add_url_rule('/posts/<author_username>','get_posts_by_author',get_posts_by_author,methods=['GET'])
    app.add_url_rule('/posts/<post_id>','get_post_by_id',get_post_by_id,methods=['GET'])
    app.add_url_rule('/posts', 'create_post', create_post, methods=['POST'])
    app.add_url_rule('/posts/<post_id>', 'update_post', update_post, methods=['PUT'])
    app.add_url_rule('/posts/<post_id>', 'delete_post', delete_post, methods=['DELETE'])
    app.add_url_rule('/posts/<post_id>/<vote_type>', 'vote_post', vote_post, methods=['POST'])
    app.add_url_rule('/posts/<post_id>/comments', 'add_comment', add_comment, methods=['POST'])
    app.add_url_rule('/posts/<post_id>/comments/<comment_id>', 'delete_comment', delete_comment, methods=['DELETE'])
    
    # Suggestions routes
    app.add_url_rule('/suggestions/<username>', 'get_user_suggestions', get_user_suggestions, methods=['GET'])
    
    # Landing page route
    app.add_url_rule('/', 'index', index)
