# system.py

import random

class PoliticalSystem:
    def __init__(self):
        self.government = "Democratic Republic"
        self.electoral_system = "Proportional Representation"
        self.political_parties = {}
        self.parliament_seats = 100  # Default total number of seats in parliament
    
    def add_party(self, party_name, votes):
        """Add a political party with a certain number of votes."""
        self.political_parties[party_name] = votes
    
    def change_government(self, new_government):
        """Change the type of government."""
        self.government = new_government
    
    def set_electoral_system(self, electoral_system):
        """Change the electoral system."""
        self.electoral_system = electoral_system
    
    def simulate_election(self):
        """Simulate an election based on the chosen electoral system."""
        total_votes = sum(self.political_parties.values())
        results = {}
        
        if self.electoral_system == "Proportional Representation":
            for party, votes in self.political_parties.items():
                # Calculate the seats based on proportion of total votes
                seats = (votes / total_votes) * self.parliament_seats
                results[party] = round(seats)
        
        elif self.electoral_system == "Majoritarian":
            # Simulate a winner-takes-all system (e.g., first-past-the-post)
            winner = max(self.political_parties, key=self.political_parties.get)
            results[winner] = self.parliament_seats  # Winner takes all seats

        return results

    def get_current_state(self):
        """Return the current state of the political system."""
        return {
            "Government": self.government,
            "Electoral System": self.electoral_system,
            "Political Parties": self.political_parties,
        }
