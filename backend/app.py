from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('scores.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    with open('schema.sql', 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

@app.route('/api/score', methods=['POST'])
def save_score():
    try:
        data = request.get_json()
        telegram_id = data.get('telegram_id')
        score = data.get('score')
        
        if not telegram_id or score is None:
            return jsonify({'error': 'Missing data'}), 400
        
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO scores (telegram_id, score) VALUES (?, ?)',
            (telegram_id, score)
        )
        conn.commit()
        conn.close()
        
        return jsonify({'ok': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/top', methods=['GET'])
def get_top_scores():
    try:
        conn = get_db_connection()
        scores = conn.execute('''
            SELECT telegram_id, score, created_at 
            FROM scores 
            ORDER BY score DESC 
            LIMIT 10
        ''').fetchall()
        conn.close()
        
        result = []
        for score in scores:
            result.append({
                'telegram_id': score['telegram_id'],
                'score': score['score'],
                'created_at': score['created_at']
            })
        
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)