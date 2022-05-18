import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

jackson_family = FamilyStructure("Jackson")

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<member_id>', methods=['GET'])
def get_this_member(member_id):
    member = jackson_family.get_member(member_id)
    return jsonify(member), 200

@app.route('/member', methods=['POST'])
def new_member():
    member = request.get_json()
    sucess = jackson_family.add_member(member)
    if sucess == True:
        return jsonify('Nuevo miembro agregado'), 200
    else:
        return jsonify('Algo salió mal'), 400

@app.route('/member/<member_id>', methods=['DELETE'])
def delete_a_member(member_id):
    return jsonify(jackson_family.delete_member(member_id)), 200

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
