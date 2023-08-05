import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
import requests

def _get_pokemon_data(name):
    """
    Fetches the data for a pokemon from the Poké API. 
    """
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + name.lower())
    if response.status_code == 200:
        response = response.json()
        pokemon = { 
            'name': response['name'],
            'id': response['id'],
            'height': response['height'],
            'weight': response['weight'],
            'types': [t['type']['name'] for t in response['types']],
            'abilities': [a['ability']['name'] for a in response['abilities']],
            
            }
    else:
        return None
    return pokemon

class PokeConnection(st.connections.ExperimentalBaseConnection):
    """
    A connection class to fetch pokemon data from the Poké API.

    Attributes:
        connection_name (str): The name of the connection (optional).
    """
    connection_name = 'Poke'

    def _connect(self):
        """
        Connects to the Poké API.
        """
        pass

    def query(self, connection_name, name):
        """
        Queries the Poké API for the pokemon matching the query.
        """
        @st.cache_data(ttl=600)
        def _get_pokemon_data_cached(name):
            return _get_pokemon_data(name)

        return _get_pokemon_data_cached(name)

