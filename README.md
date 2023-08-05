# Streamlit Connections Hackathon 🎈
## Poké API ⚡
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pokemonapp.streamlit.app)

Welcome to the Pokémon search and information app! With this app, you can easily find information about your favorite Pokémon, including their stats, evolutions, and more. This app is designed to be fast and easy to use, so you can quickly find the information you need.

With PokeConnection you can retrieve Pokémon data from the Poké API:

```python
import streamlit as st
conn = st.experimental_connection("poke", type=PokeConnection)
pokemon_name = "charmander"
pokemon = conn.query("pokemon", name=pokemon_name)
st.write("Abilities:", ', '.join(pokemon['abilities']))
```
Feel free to fork this repository and add new features! 


🥳 You're all set and ready to get information from your favorite Pokémon!
