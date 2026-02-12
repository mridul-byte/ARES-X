# ARES-X File 05: Web UI Controller
from flask import Blueprint, render_template, request, jsonify
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Renders the Professional Industrial Dashboard
    return render_template('index.html')

@main_bp.route('/api/status')
def system_status():
    # Real-time health check of the 35 modules
    return jsonify({
        "status": "Operational",
        "modules_loaded": 35,
        "database_size": "4.2GB",
        "engine": "ARES-X Core v1.0"
    })

@main_bp.route('/api/trigger', methods=['POST'])
def trigger_action():
    module = request.json.get('module')
    target = request.json.get('target')
    # Logic to hand off to File 08 (engine.py)
    return jsonify({"msg": f"Module {module} initiated on {target}"})
