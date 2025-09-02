from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv
load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.config')

    db.init_app(app)

    from routes.builds import builds_bp
    from routes.deployments import deployments_bp
    from routes.alerts import alerts_bp

    app.register_blueprint(builds_bp, url_prefix='/builds')
    app.register_blueprint(deployments_bp, url_prefix='/deployments')
    app.register_blueprint(alerts_bp, url_prefix='/alerts')

    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)