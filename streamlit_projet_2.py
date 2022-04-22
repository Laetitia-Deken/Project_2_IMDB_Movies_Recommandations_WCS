import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import streamlit as st

from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

import unicodedata # pour enlever les accents

import pickle


@st.cache(show_spinner=False, suppress_st_warning=True)
def initialization():
    selection = pd.read_csv("Etape_3_selection.csv")  #join.csv est notre dataset final
    data_selection = pd.read_csv("Etape_1_selection.csv")

    ## 2.1. Choix de X et uniformisation

    X = selection[selection.select_dtypes("number").columns]
    scaler = StandardScaler()
    scaler.fit(X)
    X_scaler = scaler.transform(X)
    X_scaler = pd.DataFrame(X_scaler, columns=selection.select_dtypes("number").columns)

    ## 2.2. Entraînement  du model et picklization !!!

    # distance = NearestNeighbors(n_neighbors=6).fit(X_scaler)
    # pickle.dump(distance, open('distance.pkl', 'wb'))

    distance = pickle.load(open('distance.pkl', 'rb'))

    return selection, X_scaler, distance, data_selection

def choix_page():
    pages = {
        "Accueil": accueil,
        "Recommandation": recommandation,
        "Visualisation": visu
    }
    
    with st.sidebar:
        page = st.selectbox("Choisir une page :", list(pages.keys()))
    
    pages[page]()
    
def accueil():
    st.write("Choisir une page sur la gauche")
    
def recommandation():
    st.write(reco_film(data=selection, x_scaler=X_scaler, model=distance))

def visu():
    pass

### 2.3.1. Fonction d'affichage

def display(search, model, data, x_scale, titre):
    """
    input: search : array of funded index
           model : trained model
           data : the dataframe with movies
           x_scale : X value
           titre : title from input user
    """
    x_scaler = x_scale
    title = titre
    search_index = search.index
    
    if len(search) == 1:
        proches_title = model.kneighbors(x_scaler.iloc[search_index])
        st.write(f"""\nLes 5 films que vous nous recommandons pour \
\"{data.iloc[search_index[0]]['title_fr']}\" sorti en \
{int(data.iloc[search_index]['startYear'])} :\n""")
        
        for x in range(1, len(proches_title[1][0])):
            result = data.iloc[proches_title[1][0][x]]
            st.write(f'\tFilm numéro {x} :', result.loc["title_fr"] if result.loc["title_fr"] != '~'
                  else result.loc["originalTitle"], f'de {int(result.loc["startYear"])}')
            print()
        return True
    elif len(search) > 1:
        st.write(f"\nNous avons trouvé {len(search)} films indiquez le film souhaité :\n")

#         for choix in range(len(search)):
#             st.write(f"""Choix {choix + 1} : {data.iloc[search.index[choix]]['title_fr']} \
# sorti en {int(data.iloc[search.index[choix]]['startYear'])}""")

        choix_user = st.selectbox("Sélectionnez un film dans la liste", ["Sélectionnez un film dans la liste"] + list(search['title_fr']))
        
        if choix_user != "Sélectionnez un film dans la liste":
        #     st.write("Sélectionnez un film !!!!")
            
            index = search[search['title_fr'] == choix_user].index
            # Forget verification on choix_user
            
            proches_title = model.kneighbors([x_scaler.iloc[index[0]]])
            st.write(f"""\nLes 5 films que vous nous recommandons pour \
    \"{search[search['title_fr'] == choix_user]['title_fr'].to_string(index=False)}\" de {int(search[search['title_fr'] == choix_user]['startYear'])} : \n""")
        
            for x in range(1, len(proches_title[1][0])):
                result = data.iloc[proches_title[1][0][x]]
                st.write(f'\tFilm numéro {x} :', result.loc["title_fr"] if result.loc['title_fr'] != '~'
    else f"{result.loc['originalTitle']} (Titre en VO)",f'de {int(result.loc["startYear"])} ')
                print()
            return True
            
    else:
        return False
        
        

### 2.3.2. Fonction pour avoir des recommandations

def reco_film(data, x_scaler, model):
    """ 
        data = df selection de films features
        x_scaler = Features scaled
        model = Trained model
        return = nom 5 films proches voisins 
    
    """
    
    title_input = st.text_input('Entrer un titre de film', " ", placeholder="Entrer un titre de film")
    
    distance = model
    # Transform input to lower, strip and without accent
    if title_input != " ":
        nfkd_form = unicodedata.normalize('NFKD', title_input).strip()
        title = u"".join([c for c in nfkd_form if not unicodedata.combining(c)]).strip().lower()
        search = data.loc[data['title'] == title]
        if len(search) > 0:
            if(display(search, distance, data, x_scaler, title)):
                return f"Toute l'équipe de WildSalto vous souhaite Bon visionnage !!"

        else:
            search_2 = data.loc[data['title'].str.contains(title)]
            if(display(search_2, distance, data, x_scaler, title)):
                return f"""Toute l'équipe de WildSalto vous souhaite Bon visionnage !!
            Voulez-vous avoir une nouvelle recommandation ?
            """
            else:
                return str('Voulez-vous avoir une nouvelle recommandation ?')
    else:
        return "Entrez un titre de film !"       
# st.write(reco_film(data=selection, x_scaler=X_scaler, model=distance))

if __name__ == "__main__":
    selection, X_scaler, distance, data_selection = initialization()
    choix_page()
    