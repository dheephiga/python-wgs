from app import db, Match
from app import app

# Sample data for matches
more_matches_data = [
    {'team1': 'Team G', 'team2': 'Team H', 'venue': 'Stadium 4', 'status': 'Live'},
    {'team1': 'Team I', 'team2': 'Team J', 'venue': 'Stadium 5', 'status': 'Upcoming'},
    {'team1': 'Team K', 'team2': 'Team L', 'venue': 'Stadium 6', 'status': 'Finished'},
    # Add more sample data as needed
]

# Add more sample matches to the database
with app.app_context():
    for match_info in more_matches_data:
        match = Match(team1=match_info['team1'], team2=match_info['team2'], venue=match_info['venue'], status=match_info['status'])
        db.session.add(match)

    # Commit the changes to the database
    db.session.commit()

print("More sample data added successfully.")
