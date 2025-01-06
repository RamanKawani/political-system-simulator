# app.py
import streamlit as st
from system import PoliticalSystem

def app():
    st.title("Custom Political System Tree Builder")
    
    # Initialize the political system
    system = PoliticalSystem()
    
    # Show the current state of the system (tree structure)
    st.header("Current Political System Tree")
    state = system.get_current_state()
    
    # Display the system tree
    system.print_tree(state)
    
    # Change Government Type
    st.header("Change Government Type")
    government_type = st.selectbox(
        "Select Government Type", 
        options=["Democratic Republic", "Monarchy", "Authoritarian"]
    )
    if st.button("Change Government"):
        system.set_value("Government Type", government_type)
        st.success(f"Government changed to {government_type}")
    
    # Set Electoral System
    st.header("Set Electoral System")
    electoral_system = st.selectbox(
        "Select Electoral System", 
        options=["Proportional Representation", "Majoritarian"]
    )
    if st.button("Set Electoral System"):
        system.set_value("Electoral System", electoral_system)
        st.success(f"Electoral system changed to {electoral_system}")
    
    # Add Political Parties
    st.header("Add Political Parties")
    party_name = st.text_input("Enter Party Name")
    if st.button("Add Party"):
        system.set_value("Political Parties", party_name)
        st.success(f"Party {party_name} added.")
    
    # Set Neo-Traditional System
    st.header("Set Neo-Traditional System")
    neo_traditional_system = st.selectbox(
        "Select Neo-Traditional System", 
        options=["None", "Tribal Council", "Chiefdom"]
    )
    if st.button("Set Neo-Traditional System"):
        system.set_value("Neo-Traditional Systems", neo_traditional_system)
        st.success(f"Neo-Traditional system set to {neo_traditional_system}")
    
# Run the app
if __name__ == "__main__":
    app()
