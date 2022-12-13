utilisateurs = {
  "user1": "password1",
  "user2": "password2",
  "user3": "password3"
}

# Fonction de login
def login(username, password):
  if username in utilisateurs and utilisateurs[username] == password:
    # Si les informations d'identification sont valides, retourner True
    return True
  else:
    # Sinon, retourner False
    return False

# Programme principal
if __name__ == "__main__":
  # Demander à l'utilisateur de saisir son nom d'utilisateur et son mot de passe
  username = input("Entrez votre nom d'utilisateur : ")
  password = input("Entrez votre mot de passe : ")
  
  # Vérifier les informations d'identification
  if login(username, password):
    print("Connexion réussie.")
  else:
    print("Connexion échouée.")
