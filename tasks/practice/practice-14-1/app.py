from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cricket.db'
db = SQLAlchemy(app)

# Define your database models
class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team1 = db.Column(db.String(100), nullable=False)
    team2 = db.Column(db.String(100), nullable=False)
    venue = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Match('{self.team1}', '{self.team2}', '{self.venue}', '{self.status}')"
with app.app_context():
    db.create_all()
# Routes for HTML pages
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

# Add more routes for team details, venue info, etc.

if __name__ == '__main__':
    app.run(debug=True)
