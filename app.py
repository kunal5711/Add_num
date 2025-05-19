from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add_numbers():
    try:
        # Get numbers from query parameters
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        
        # Calculate sum
        result = num1 + num2
        
        # Return result as JSON
        return jsonify({
            'result': result
        })
    except ValueError:
        return jsonify({'error': 'Please provide valid numbers'}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)