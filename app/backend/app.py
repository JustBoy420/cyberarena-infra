from flask import Flask, request, jsonify
import redis
import os

app = Flask(__name__)
# K8s DNS: мы обращаемся к Redis по имени сервиса redis-svc
r = redis.Redis(host=os.getenv('REDIS_HOST', 'redis-svc'), port=6379, decode_responses=True)

@app.route('/api/tickets', methods=['GET'])
def get_tickets():
    tickets = []
    for key in r.scan_iter("ticket:*"):
        tickets.append(r.hgetall(key))
    return jsonify(tickets)

@app.route('/api/tickets', methods=['POST'])
def create_ticket():
    data = request.json
    ticket_id = r.incr("ticket_id_counter")
    r.hset(f"ticket:{ticket_id}", mapping={
        "id": ticket_id, 
        "title": data.get('title', 'No title'), 
        "status": "Open"
    })
    return jsonify({"status": "success", "id": ticket_id}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
