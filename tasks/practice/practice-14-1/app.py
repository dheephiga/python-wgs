from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cricket.db'
db = SQLAlchemy(app)

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team1 = db.Column(db.String(100), nullable=False)
    team2 = db.Column(db.String(100), nullable=False)
    venue = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    score_team1 = db.Column(db.Integer, nullable=True)  
    score_team2 = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"Match('{self.team1}', '{self.team2}', '{self.venue}', '{self.status}', '{self.score_team1}', '{self.score_team2}')"
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/live_scores')
def live_scores():
    live_matches = Match.query.filter_by(status='Live').all()
    return render_template('live_scores.html', matches=live_matches)

@app.route('/upcoming_matches')
def upcoming_matches():
    upcoming_matches = Match.query.filter_by(status='Upcoming').all()
    return render_template('upcoming_matches.html', matches=upcoming_matches)


if __name__ == '__main__':
    app.run(debug=True)
