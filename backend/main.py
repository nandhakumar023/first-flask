from flask import request, jsonify
from config import app, db
from models import Contact

@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all() #->list(object), use flaskSQLALchemy(orm) to get all contacts in db
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    res = jsonify({"contacts" : json_contacts})
    return res

@app.route("/add_contacts", methods=["POST"])
def create_contact():
    name = request.json.get("name")
    email = request.json.get("email")

    if not name or not email:
        return jsonify({"Message" : "need to enter name and email"}), 400  #400 = bad requst
    
    new_contact = Contact(name=name, email=email)

    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message" : str(e)}), 400
    
    return jsonify({"message" : "contact created"}), 200

@app.route("/update_contact/<int:user_id>", methods=["PATCH"])   #if ....5000/update_contact/2 : user_id = 2
def update_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact: #if no user with id 
        return jsonify({"Message" : "User not exist!"}), 404
    
    data = request.json
    contact.name = data.get("name", contact.name)
    contact.email = data.get("email", contact.email)
    db.session.commit()

    return jsonify({"message" : "updated succes"}), 200

@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delecte_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"Message" : "User not exist!"}), 404
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message" : "contact delected"}), 200



if __name__ ==  "__main__":
    with app.app_context():
        db.create_all()  #check if db is created and initilized

    app.run(debug=True)
