from flask import Flask, request, jsonify
import data_check

app = Flask(__name__, static_folder='.')


@app.route('/')
def serve_index():
    return app.send_static_file('index.html')


@app.route('/process_text', methods=['POST'])
def process_text():
    text = request.json.get('text', '')
    matched_keywords, replaced_text = data_check.match_and_replace_sensitive_in_text(text)
    return jsonify({'matched_keywords': matched_keywords, 'replaced_text': replaced_text})


if __name__ == '__main__':
    app.run(port=5000)
