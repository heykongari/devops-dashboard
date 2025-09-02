from flask import Blueprint, render_template

deployments_bp = Blueprint('deployments', __name__)

@deployments_bp.route('/')
def show_deployments():
    deployments = [
        {'service': 'EC2', 'status': 'running'},
        {'service': 'EC2', 'status': 'stopped'}
    ]
    return render_template('deployments.html', deployments=deployments)