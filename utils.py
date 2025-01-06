# utils.py

# Example helper function
def format_parliament_results(parliament):
    return "\n".join([f"{party}: {seats} seats" for party, seats in parliament.items()])
