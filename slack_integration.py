from flask import Flask, request, jsonify
import sqlite3
import pickle
import os
import requests

app = Flask(__name__)
SLACK_TOKEN = os.getenv("SLACK_TOKEN")

# Connection parameters to local SQLite database
def get_db_connection():
    conn = sqlite3.connect('example.db')
    conn.row_factory = sqlite3.Row
    return conn

# Importing trained model and vectorizer
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# Function to push data to slack
def send_message_to_slack(channel, text):
    url = 'https://hooks.slack.com/services/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'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {SLACK_TOKEN}'
    }
    data = {
        'channel': channel,
        'text': text
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        print(f"Failed to send message: {response.text}")

# Defining actions when a POST request is received
@app.route('/slack/events', methods=['POST'])
def slack_events():
    # Reading data as dictionary (JSON)
    data = request.json
    print(f"Received data: {data}")  # Log received data

    # Respond to Slack challenge, this is for initialization
    if 'challenge' in data:
        challenge = data['challenge']
        response_data = {"challenge": challenge}
        print(f"Responding to challenge: {response_data}")
        return jsonify(response_data)

    # Parse message out of event data
    if 'event' in data:
        event_data = data['event']
        if event_data['type'] == 'message' and event_data.get('subtype') is None:
            message = event_data['text']
            print(f"Message received: {message}")  # Log received message

            try:
                # Convert message to vectorized features and predict using the model
                features = vectorizer.transform([message])
                prediction = model.predict(features)
                print(f"Prediction: {prediction}")

                # Store message and prediction in the database with timestamp
                conn = get_db_connection()
                conn.execute('INSERT INTO slack_messages (content, prediction) VALUES (?, ?)', (message, prediction[0]))
                conn.commit()
                conn.close()
                print("Message and prediction stored in database")

                # Push prediction value back to slack channel
                send_message_to_slack('#all-brians-workspace', prediction[0])

            except Exception as e:
                print(f"Error processing message: {e}")
                return jsonify({'status': 'error', 'message': str(e)}), 400

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)



