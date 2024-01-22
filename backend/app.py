import os
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from chain import Chain
from werkzeug.utils import secure_filename

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
chain = Chain()

@app.route("/")
def index():
    return "CodeRoaster working!"

@app.route("/getRoasted", methods=["POST"])
@cross_origin()
def roast_code():
    try:
        if "code" not in request.json:
            raise ValueError("No code provided in the request")
        
        code = request.json["code"]
        if not code.strip():
            raise ValueError("Empty code snippet")
        
        chain.load_data(code)
        summary = chain.get_result()
        print(summary)
        return jsonify({"summary": summary}), 200
    
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500




if __name__ == "__main__":
    app.run()