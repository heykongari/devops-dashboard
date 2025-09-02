import os

class config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dashboard.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JENKINS_URL = os.getenv("JENKINS_URL")
    JENKINS_USER = os.getenv('JENKINS_USER')
    JENKINS_TOKEN = os.getenv("JENKINS_TOKEN")
    JENKINS_JOB = os.getenv('JENKINS_JOB')