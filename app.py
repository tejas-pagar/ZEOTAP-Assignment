from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eligibility.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String, nullable=False)
    salary = db.Column(db.Float, nullable=False)
    experience = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<User {self.user_id}>'

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    try:
        new_user = User(
            user_id=data['user_id'],
            age=int(data['age']),
            department=data['department'],
            salary=float(data['salary']),
            experience=int(data['experience'])
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "Data saved successfully."})
    except Exception as e:
        return jsonify({"message": "An error occurred: " + str(e)}), 500

if __name__ == "__main__":
    
    with app.app_context():
        db.create_all()
    app.run(debug=True)
