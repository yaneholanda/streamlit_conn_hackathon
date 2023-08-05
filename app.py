import streamlit as st
from connection_pokeapi import PokeConnection
from PIL import Image

st.title("Connections Hackathon :balloon:")
st.subheader("Poké API :zap:")
st.write("Welcome to the Pokémon search and information app! With this app, you can easily find information about your favorite Pokémon, including their stats, evolutions, and more. This app is designed to be fast and easy to use, so you can quickly find the information you need.")

# Dictionary to map each Pokémon type to its corresponding emoji code or name
type_emojis = {
    "normal": "😊",
    "fire": "🔥",
    "water": "💧",
    "electric": "⚡️",
    "grass": "🍃",
    "ice": ":snowman:"
    # Add more types and their emojis as needed
}

conn = st.experimental_connection("poke", type=PokeConnection)

def get_pokemon():
    st.sidebar.image("images/icon.png", use_column_width=True)
    st.sidebar.markdown("<h2 style='text-align: center;'>Enter the name of the Pokemon:</h2>", unsafe_allow_html=True)
    pokemon_name = st.sidebar.text_input("", key="pokemon_name")
    image = Image.open(f'images/pokemon.png')
    st.image(image, caption='Pokémon')
    if pokemon_name:
        pokemon = conn.query("pokemon", name=pokemon_name)
        if pokemon and bool(pokemon):
            pokemon_type = pokemon['types'][0].lower()
            st.sidebar.markdown("<h2 style='text-align: center;'> Attributes</h2>", unsafe_allow_html=True)
            st.sidebar.write("Name:", pokemon['name'].capitalize())
            if pokemon_type in type_emojis:
                st.sidebar.write("Pokémon type:", {type_emojis[pokemon_type]})
            else:
                st.sidebar.write("Pokémon type:", pokemon_type)
            st.sidebar.write("Height:", pokemon['height'])
            st.sidebar.write("Weight:", pokemon['weight'])
            st.sidebar.write("Abilities:", ', '.join(pokemon['abilities']))
        else:
            st.write("The Pokemon you entered is not in the database")
            
    else:
        st.write("You must enter a Pokemon name")

if __name__ == "__main__":
    get_pokemon()
