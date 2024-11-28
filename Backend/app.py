# backend/app.py
from flask import Flask, request, jsonify
from models import db, Record

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///records.db'
db.init_app(app)

@app.route('/add_record', methods=['POST'])
def add_record():
    data = request.json
    new_record = Record(patient_id=data['patientId'], data_hash=data['dataHash'])
    db.session.add(new_record)
    db.session.commit()
    return jsonify({'message': 'Record added'}), 201

if __name__ == '__main__':
    app.run(debug=True)