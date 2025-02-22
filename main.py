from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# Facebook Graph API URL
FB_GRAPH_API_URL = 'https://graph.facebook.com/v15.0'


@app.route('/', methods=['GET', 'POST'])
def home():
    groups = []
    error = None
    user_name = None
    
    if request.method == 'POST':
        access_token = request.form.get('access_token')

        if access_token:
            # Fetch user's profile name to verify token validity
            profile_url = f"{FB_GRAPH_API_URL}/me?access_token={access_token}"
            profile_response = requests.get(profile_url)
            profile_data = profile_response.json()

            if 'error' in profile_data:
                # If there is an error in the response, show the invalid token message
                error = "Invalid token, please enter a working token."
            else:
                # Get the user's name from the profile data
                user_name = profile_data.get('name', 'Unknown User')

                # Fetch groups from Facebook Graph API
                groups_url = f"{FB_GRAPH_API_URL}/me/groups?access_token={access_token}"
                response = requests.get(groups_url)
                groups_data = response.json()

                if 'data' in groups_data:
                    # Prepare group list
                    groups = [{'name': group['name'], 'id': group['id']} for group in groups_data['data']]
                else:
                    error = "No groups found or an error occurred while fetching groups."
    
    # HTML template with form, error message, user name, and group list
    index_html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Koja-xD WEB / MESSENGER GROUP CHECKER</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        <style>
            body {
                background-color: #1a202c;
                color: #f9f9f9;
                font-family: Arial, sans-serif;
            }
            .container {
                max-width: 800px;
                margin-top: 50px;
            }
            .card {
                margin-bottom: 20px;
                background-color: #2d3748;
                border: 1px solid #4a5568;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .card-body {
                padding: 20px;
            }
            .card-title {
                font-size: 1.5rem;
                margin-bottom: 1rem;
            }
            .form-group {
                margin-bottom: 1rem;
            }
            .form-control {
                display: block;
                width: 100%;
                padding: 0.375rem 0.75rem;
                font-size: 1rem;
                line-height: 1.5;
                color: #f9f9f9;
                background-color: #4a5568;
                border: 1px solid #4a5568;
                border-radius: 0.25rem;
            }
            .form-control:focus {
                border-color: #eab308;
                outline: none;
                box-shadow: 0 0 0 0.2rem rgba(234, 179, 8, 0.25);
            }
            .btn-group {
                display: flex;
                justify-content: space-between;
            }
            .btn-neon {
                color: #fff;
                background-color: #ffcc33;
                box-shadow: 0 0 10px #ffcc33, 0 0 40px #ffcc33, 0 0 80px #ffcc33;
                border-radius: 20px;
                font-weight: bold;
                cursor: pointer;
                transition: all 0.5s ease;
            }
            .btn-neon:hover {
                box-shadow: 0 0 5px #ffcc33, 0 0 20px #ffcc33, 0 0 40px #ffcc33, 0 0 80px #ffcc33;
            }

            /* Animation for blinking and color change */
            @keyframes blink {
                0%, 100% {
                    opacity: 1;
                    color: #ffcc33;  /* Bright yellow */
                }
                25% {
                    opacity: 0.5;
                    color: #f00;     /* Red */
                }
                50% {
                    opacity: 1;
                    color: #00ff00;  /* Green */
                }
                75% {
                    opacity: 0.5;
                    color: #00f;     /* Blue */
                }
            }
            .animated-title {
                animation: blink 1.5s infinite; /* Slightly slower animation */
                font-size: 1.5rem;
            }

            /* New styles for group list items */
            .group-list {
                background-color: rgba(255, 255, 255, 0.1); /* Transparent background */
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Shadow around the group list */
                padding: 15px;
            }
            .list-group-item {
                background-color: transparent; /* Transparent background for each list item */
                color: #f9f9f9; /* Ensure text is visible */
                border: none; /* Remove default border */
                margin-bottom: 10px; /* Space between items */
                padding: 10px; /* Padding inside items */
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h3 class="text-center mb-4">MESSENGER GROUP CHECKER</h3>
            <div class="card">
                <div class="card-body">
                    <h2 class="card-title">Enter Your Facebook Access Token</h2>
                    <form method="post" action="/">
                        <div class="form-group">
                            <label for="access_token">ACCESS TOKEN:</label>
                            <input type="text" class="form-control" id="access_token" name="access_token" required>
                        </div>
                        {% if error %}
                            <p style="color:red;">{{ error }}</p>
                        {% endif %}
                        <div class="btn-group">
                            <button type="submit" class="btn btn-neon mt-3">GET GROUPS</button>
                        </div>
                    </form>
                </div>
            </div>

            {% if user_name %}
            <div class="card mt-4">
                <div class="card-body">
                    <h3 class="card-title">Profile Name: {{ user_name }}</h3>
                </div>
            </div>
            {% endif %}

            {% if groups %}
            <div class="card mt-4">
                <div class="card-body group-list">
                    <h3 class="card-title animated-title">Your Facebook Groups</h3>
                    <ul class="list-group">
                        {% for group in groups %}
                            <li class="list-group-item">
                                <strong>{{ group.name }}</strong> (ID: {{ group.id }})
                            </li>
                        {% endfor %}
                    </ul>
                </div>
            </div>
            {% endif %}
        </div>
    </body>
    </html>
    '''
    return render_template_string(index_html, error=error, groups=groups, user_name=user_name)


if __name__ == '__main__':
    app.run(debug=True)
