from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..extensions import db
from ..models.bounty import Bounty

bp = Blueprint('bounty', __name__)

@bp.route('/create-bounty', methods=['POST'])
@jwt_required()
def create_bounty():
    data = request.get_json()
    project_id = data.get('project_id')
    amount = data.get('amount')
    creator_id = get_jwt_identity()
    new_bounty = Bounty(project_id=project_id, amount=amount, creator_id=creator_id)
    db.session.add(new_bounty)
    db.session.commit()
    return jsonify({"msg": "Bounty created successfully"}), 201

@bp.route('/claim-bounty', methods=['POST'])
@jwt_required()
def claim_bounty():
    data = request.get_json()
    bounty_id = data.get('bounty_id')
    claimer_id = get_jwt_identity()
    bounty = Bounty.query.filter_by(id=bounty_id, claimed_by=None).first()
    if bounty:
        bounty.claimed_by = claimer_id
        db.session.commit()
        return jsonify({"msg": "Bounty claimed successfully"}), 200
    return jsonify({"msg": "Bounty not found or already claimed"}), 404
