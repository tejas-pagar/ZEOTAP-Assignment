# app.py

from flask import Flask, request, jsonify, render_template
from models import db, Rule, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rules_engine.db'  # Use SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()  # Create database tables

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rules', methods=['POST'])
def add_rule():
    data = request.get_json()
    rule_string = data.get('rule')

    if not rule_string:
        return jsonify({"error": "Rule string is required!"}), 400

    new_rule = Rule(rule_string=rule_string)
    db.session.add(new_rule)
    db.session.commit()

    return jsonify({"message": "Rule added successfully!", "rule_id": new_rule.id})

@app.route('/rules/<int:rule_id>/modify', methods=['POST'])
def modify_rule(rule_id):
    data = request.get_json()
    rule = Rule.query.get(rule_id)

    if not rule:
        return jsonify({"error": "Rule not found!"}), 404

    if 'new_rule_string' in data:
        rule.rule_string = data['new_rule_string']

    db.session.commit()
    return jsonify({"message": "Rule modified successfully!"})

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = data.get('user_id')
    user_data = data.get('user_data')

    if not user_id or not user_data:
        return jsonify({"error": "User ID and data are required!"}), 400

    new_user = User(user_id=user_id, **user_data)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User data added successfully!"})

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.get_json()
    user_id = data.get('user_id')

    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        return jsonify({"error": "User not found!"}), 404

    # Here you would evaluate the user's eligibility against the rules
    is_eligible = False  # Replace with actual eligibility logic

    return jsonify({"user_id": user_id, "isEligible": is_eligible})

if __name__ == '__main__':
    app.run(debug=True)
