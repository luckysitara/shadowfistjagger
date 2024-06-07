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
from .extensions import w3

@bp.route('/submit-project', methods=['POST'])
@jwt_required()
def submit_project():
    data = request.get_json()
    project_id = data.get('project_id')
    details = data.get('details')
    owner_id = get_jwt_identity()
    new_project = Project(project_id=project_id, details=details, owner_id=owner_id)

    # Interact with Solana smart contract
    # Assuming you have the contract ABI and address
    contract = w3.eth.contract(address='YOUR_CONTRACT_ADDRESS', abi='YOUR_CONTRACT_ABI')
    tx_hash = contract.functions.submitProject(project_id, details).transact({'from': owner_id})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    if receipt.status:
        db.session.add(new_project)
        db.session.commit()
        return jsonify({"msg": "Project submitted successfully"}), 201
    else:
        return jsonify({"msg": "Failed to submit project on blockchain"}), 500
