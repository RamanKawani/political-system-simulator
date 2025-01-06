# app.py
import streamlit as st
from system import PoliticalSystem

def app():
    st.title("Custom Political System Simulator")
    
    # Initialize the political system
    system = PoliticalSystem()
    
    # Show the current state of the system
    st.header("Current Political System")
    state = system.get_current_state()
    st.write(state)
    
    # Change government type
    st.header("Change Government Type")
    new_government = st.selectbox(
        "Select Government Type", 
        options=["Democratic Republic", "Monarchy", "Authoritarian", "Republic"]
    )
    if st.button("Change Government"):
        system.change_government(new_government)
        st.success(f"Government changed to {new_government}")
    
    # Set electoral system
    st.header("Set Electoral System")
    electoral_system = st.selectbox(
        "Select Electoral System", 
        options=["Proportional Representation", "Majoritarian"]
    )
    if st.button("Change Electoral System"):
        system.set_electoral_system(electoral_system)
        st.success(f"Electoral system changed to {electoral_system}")
    
    # Add political parties
    st.header("Add a Political Party")
    party_name = st.text_input("Enter Party Name")
    party_votes = st.number_input("Enter Number of Votes", min_value=0, max_value=1000000)
    if st.button("Add Party"):
        if party_name and party_votes >= 0:
            system.add_party(party_name, party_votes)
            st.success(f"Added party {party_name} with {party_votes} votes.")
    
    # Simulate Election
    st.header("Simulate Election")
    if st.button("Simulate Election"):
        results = system.simulate_election()
        st.write("Election Results (Seats Allocation):")
        for party, seats in results.items():
            st.write(f"{party}: {seats} seats")
    
# Run the app
if __name__ == "__main__":
    app()
