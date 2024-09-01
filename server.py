from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chabiloge():
  url = "https://denver1769.shodns.in/ChabiLoge.php"

  try:
    response = requests.post(url)
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

    return f"Response status code: {response.status_code}\nResponse HTML body: {response.text}"

  except requests.exceptions.RequestException as e:
    return f"Error: {e}", 500

if __name__ == "__main__":
  port = int(os.environ.get('PORT', 5000))
  app.run(debug=True, host='0.0.0.0', port=port) 
