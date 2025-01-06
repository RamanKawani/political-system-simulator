import streamlit as st
import numpy as np
import pandas as pd

# Define functions for simulating the political system
def create_government():
    government = {
        'President': 'John Doe',
        'Ministers': ['Minister of Finance', 'Minister of Defense', 'Minister of Health']
    }
    return government

def create_parties():
    parties = {
        'Party A': 'Conservative',
        'Party B': 'Liberal',
        'Party C': 'Socialist'
    }
    return parties

def simulate_election(parties):
    # Simple election simulation based on random votes
    results = {party: np.random.randint(100, 1000) for party in parties}
    return results

# Streamlit app layout
st.title('Political System Simulator')

# Sidebar for user interaction
st.sidebar.header('Simulation Settings')
simulation_type = st.sidebar.selectbox('Select Simulation Type', ['Create Government', 'Political Parties', 'Election'])

if simulation_type == 'Create Government':
    st.subheader('Government Overview')
    government = create_government()
    st.write(f"President: {government['President']}")
    st.write(f"Ministers: {', '.join(government['Ministers'])}")
    
    # Allow user to add new ministers
    new_minister = st.text_input('Add a new minister', '')
    if new_minister:
        government['Ministers'].append(new_minister)
        st.write(f"Updated Ministers: {', '.join(government['Ministers'])}")
        
elif simulation_type == 'Political Parties':
    st.subheader('Political Parties Overview')
    parties = create_parties()
    st.write(f"Political Parties and Ideologies:")
    for party, ideology in parties.items():
        st.write(f"{party}: {ideology}")
    
    # Allow user to add a new party
    new_party = st.text_input('Add a new political party', '')
    new_ideology = st.text_input('Add party ideology', '')
    if new_party and new_ideology:
        parties[new_party] = new_ideology
        st.write(f"Updated Political Parties:")
        for party, ideology in parties.items():
            st.write(f"{party}: {ideology}")

elif simulation_type == 'Election':
    st.subheader('Election Simulation')
    parties = create_parties()
    election_results = simulate_election(parties)
    
    # Display election results
    st.write("Election Results:")
    for party, votes in election_results.items():
        st.write(f"{party}: {votes} votes")
    
    # Show results in a bar chart
    election_df = pd.DataFrame(list(election_results.items()), columns=["Party", "Votes"])
    st.bar_chart(election_df.set_index("Party"))
    
    # Allow user to simulate another election
    if st.button('Simulate New Election'):
        election_results = simulate_election(parties)
        st.write("New Election Results:")
        for party, votes in election_results.items():
            st.write(f"{party}: {votes} votes")
        election_df = pd.DataFrame(list(election_results.items()), columns=["Party", "Votes"])
        st.bar_chart(election_df.set_index("Party"))
