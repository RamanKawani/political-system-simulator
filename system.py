# system.py
class PoliticalSystem:
    def __init__(self):
        self.government = "Democratic"
        self.political_parties = ["Party A", "Party B", "Party C"]
        self.parliament = {
            "Party A": 50,
            "Party B": 30,
            "Party C": 20
        }
    
    def change_government(self, new_government):
        self.government = new_government

    def add_party(self, party_name, seats):
        self.political_parties.append(party_name)
        self.parliament[party_name] = seats
    
    def simulate_vote(self):
        # Simulate a simple election based on the largest number of seats
        winning_party = max(self.parliament, key=self.parliament.get)
        return winning_party
