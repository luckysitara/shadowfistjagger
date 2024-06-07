from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..extensions import db
from ..models.project import Project

bp = Blueprint('project', __name__)

@bp.route('/submit-project', methods=['POST'])
@jwt_required()
def submit_project():
    data = request.get_json()
    project_id = data.get('project_id')
    details = data.get('details')
    owner_id = get_jwt_identity()
    new_project = Project(project_id=project_id, details=details, owner_id=owner_id)
    db.session.add(new_project)
    db.session.commit()
    return jsonify({"msg": "Project submitted successfully"}), 201
