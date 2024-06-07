from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..extensions import db
from ..models.bug import Bug

bp = Blueprint('bug', __name__)

@bp.route('/report-bug', methods=['POST'])
@jwt_required()
def report_bug():
    data = request.get_json()
    project_id = data.get('project_id')
    description = data.get('description')
    reporter_id = get_jwt_identity()
    new_bug = Bug(project_id=project_id, description=description, reporter_id=reporter_id)
    db.session.add(new_bug)
    db.session.commit()
    return jsonify({"msg": "Bug reported successfully"}), 201
