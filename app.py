from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    print('im here')
    file = request.files['file']
    if file:
        # Replace with your actual Azure function URL
        azure_function_url = 'https://my-test-func001.azurewebsites.net/api/file'
        
        files = {'file': (file.filename, file.stream, file.content_type)}
        try:
            response = requests.post(azure_function_url, files=files)
            return response.text
        except Exception as e:
            return f"An error occurred: {str(e)}"
    return "No file selected."


if __name__ == '__main__':
    app.run(debug=True)
