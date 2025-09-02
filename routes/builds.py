from flask import Blueprint, render_template, current_app
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime

builds_bp = Blueprint('builds', __name__)

@builds_bp.route('/')
def show_builds():
    jenkins_url = current_app.config['JENKINS_URL']
    jenkins_user = current_app.config['JENKINS_USER']
    jenkins_token = current_app.config['JENKINS_TOKEN']
    jenkins_job = current_app.config['JENKINS_JOB']
    api_url = (
        f"{jenkins_url}/job/{jenkins_job}/api/json"
        "?tree=builds[number,result,timestamp,actions[parameters[name,value]]]"
    )

    try:
        response = requests.get(api_url, auth=HTTPBasicAuth(jenkins_user,jenkins_token), timeout=10)
        response.raise_for_status()
        data = response.json()

        builds = []
        for build in data.get('builds', [])[:10]:
            
            timestamp = datetime.fromtimestamp(build["timestamp"]/1000).strftime("%Y-%m-%d %H:%M:%S")
            
            builds.append({
                'id': build['number'],
                'status': build.get('result', 'IN PROGRESS'),
                'timestamp': timestamp
            })

    except Exception as e:
        builds = []
        print(f"Error fetching builds: {e}")

    return render_template('builds.html', builds=builds)