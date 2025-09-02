from flask import Blueprint, render_template

alerts_bp = Blueprint('alerts', __name__)

@alerts_bp.route('/')
def show_alerts():
    alerts = [
        {'message': 'Build #2 failed on dev branch', 'level': 'critical'},
        {'message': 'EC2 instance stopped', 'level': 'warning'}
    ]
    return render_template('alerts.html', alerts=alerts)