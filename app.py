# app.py
import streamlit as st
from system import PoliticalSystem

def app():
    st.title("Political System Simulator")
    
    # Initialize the PoliticalSystem object
    system = PoliticalSystem()
    
    st.header("Current Government System:")
    st.write(system.government)
    
    st.header("Political Parties and Seats in Parliament:")
    st.write(system.parliament)
    
    st.header("Change Government Type")
    new_government = st.selectbox(
        "Choose a government type", 
        options=["Democratic", "Authoritarian", "Republic", "Monarchy"]
    )
    if st.button("Change Government"):
        system.change_government(new_government)
        st.success(f"Government changed to {new_government}")
    
    st.header("Simulate Election Results")
    if st.button("Simulate Vote"):
        winner = system.simulate_vote()
        st.success(f"The winning party is {winner}")

    st.header("Add a New Party")
    party_name = st.text_input("Enter Party Name")
    party_seats = st.number_input("Enter Seats", min_value=1, max_value=500)
    
    if st.button("Add Party"):
        if party_name and party_seats:
            system.add_party(party_name, party_seats)
            st.success(f"Added {party_name} with {party_seats} seats")

# Run the app
if __name__ == "__main__":
    app()
