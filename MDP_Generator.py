import string
import secrets
import pyperclip
import time
import colorama
from colorama import Fore, Back, Style

colorama.init()

# Définition des couleurs
clr_blue = Fore.CYAN + Style.BRIGHT
clr_red = Back.RED + Style.BRIGHT
clr_dflt = Style.RESET_ALL

# Définition des ensembles de caractères
chrs = string.ascii_letters + string.digits + string.punctuation
numbers = string.digits

def generate_password(length: int) -> str:
    """Génère un mot de passe aléatoire de la longueur spécifiée."""
    return ''.join(secrets.choice(chrs) for _ in range(length))

def generate_pin(length: int) -> str:
    """Génère un PIN aléatoire de la longueur spécifiée."""
    return ''.join(secrets.choice(numbers) for _ in range(length))

def get_valid_length(prompt: str) -> int:
    """Demande à l'utilisateur de saisir une longueur valide pour le mot de passe ou le PIN."""
    while True:
        length_str = input(prompt)
        if length_str.isnumeric() and int(length_str) > 0:
            return int(length_str)
        else:
            print("Choix non valide. Veuillez rentrer un nombre valide.")

def main():
    """Fonction principale pour gérer le générateur de mot de passe et de PIN."""
    while True:
        choose = input("Qu'est-ce que tu veux générer, MDP ou pin ?: ").lower()
        
        if choose == "mdp":
            length_mdp = get_valid_length("Choisis la longueur de ton Mot De Passe: ")
            password = generate_password(length_mdp)
            print(f"Ton Mot De Passe:{clr_blue} {password}{clr_dflt}")
            pyperclip.copy(password)
            print("Ton Mot De Passe a été enregistré dans ton presse-papier")
        
        elif choose == "pin":
            length_pin = get_valid_length("Choisis la longueur de ton PIN: ")
            pin = generate_pin(length_pin)
            print(f"Ton PIN:{clr_blue} {pin}{clr_dflt}")
            pyperclip.copy(pin)
            print("Ton Code PIN a été enregistré dans ton presse-papier")
        
        else:
            print(f"{clr_red}ERROR:{clr_dflt} Choix non valide. Veuillez choisir 'MDP' ou 'PIN'.")
            continue
        
        another = input("Souhaitez-vous générer un autre Mot De Passe ou PIN ? (oui/non) : ").lower()
        if another not in ["oui", "o", "yes", "y"]:
            break
    
    print("Merci d'avoir utilisé le générateur !")
    time.sleep(1)

if __name__ == "__main__":
    main()
