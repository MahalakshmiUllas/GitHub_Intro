# from flask import Flask, request, jsonify
# import json
# import requests

# app = Flask(__name__)

# # def chuck():    
# #     f = r"https://api.chucknorris.io/jokes/random"
# #     data = requests.get(f)
# #     tt = json.loads(data.text)
    
# #     print(tt["value"]["joke"])

# # chuck()

# @app.route("/")
# def home():
#     return "hello flask data retrival"


# @app.route('/api/data')
# def get_data():
#     try:
#         response = requests.get('https://api.chucknorris.io/jokes/random')
#         # Raises an HTTPError if the HTTP request returned an unsuccessful status code
#         response.raise_for_status()  
#         data = response.json()
#         print(data)
#         data1 = jsonify(data)
#         print(data1)
#         return jsonify(data)
#     except requests.exceptions.HTTPError as http_err:
#         return jsonify({'error': f'HTTP error occurred: {http_err}'}), 500
#     except Exception as err:
#         return jsonify({'error': f'Other error occurred: {err}'}), 500
#     #return jsonify(data)




# if __name__ == "__main__":
#     app.run(port=5001)

from flask import Flask, request, jsonify

app = Flask(__name__)

# Initial list of jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the math book look sad? It had too many problems.",
    "Why do programmers prefer dark mode? Because light attracts bugs!"
]

@app.route('/joke', methods=['POST','GET'])
def create_joke():
    # Parse JSON data from the request
    data = request.get_json()
    print(data)
    if not data or 'joke' not in data:
        return jsonify({"error": "Please provide a joke in the request body."}), 400

    # Extract the joke
    new_joke = data['joke']
    jokes.append(new_joke)  # Add to the list
    return jsonify({"message": "Joke added!", "jokes": jokes}), 201

print(app.url_map)

if __name__ == '__main__':
    app.run(debug=True,port=5001)


# from flask import Flask, render_template, request, url_for, jsonify
# app = Flask(__name__)


# # @app.route('/test', methods=['GET', 'POST'])
# # def test():
# #     if request.method=='GET':
# #         return('<form action="/test" method="post"><input type="submit" value="Send" /></form>')

# #     elif request.method=='POST':
# #         return "OK this is a post method"
# #     else:
# #         return("ok")

# # @app.route('/json', methods=['POST','GET'])
# # def json():
# #     # Get the JSON data from the request
# #     data = request.get_json()
# #     # Print the data to the console
# #     print(data)
# #     # Return a success message
# #     return 'JSON received!'

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)

# from flask import Flask, request, jsonify
# import requests

# app = Flask(__name__)

# # Endpoint to get a Chuck Norris joke
# @app.route('/chucknorris/joke', methods=['POST','GET'])
# def chuck_norris_joke():
#     try:
#         # Fetch a random Chuck Norris joke from an external API
#         response = requests.get("https://api.chucknorris.io/jokes/random")
#         if response.status_code == 200:
#             joke_data = response.json()
#             return jsonify({
#                 "joke": joke_data.get("value")
#             }), 200
#         else:
#             return jsonify({
#                 "error": "Failed to fetch a joke. Please try again later."
#             }), 500
#     except Exception as e:
#         return jsonify({
#             "error": "An unexpected error occurred.",
#             "message": str(e)
#         }), 500

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)