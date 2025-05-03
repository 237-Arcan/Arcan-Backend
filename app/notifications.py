import firebase_admin
from firebase_admin import credentials, messaging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import time
from email_validator import validate_email, EmailNotValidError

# Configuration FCM (Notifications Push)
def init_fcm():
    cred = credentials.Certificate('path/to/your/firebase/credentials.json')
    firebase_admin.initialize_app(cred)

def send_push_notification(title, message, token):
    """
    Envoie une notification push via FCM.
    """
    try:
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=message
            ),
            token=token,
        )
        response = messaging.send(message)
        print(f'Notification envoyée : {response}')
    except Exception as e:
        print(f"Erreur en envoyant la notification : {e}")

# Configuration Email
def send_email(subject, body, to_email):
    """
    Envoie un email avec un sujet et un message à l'adresse spécifiée.
    """
    try:
        # Vérification de l'email
        validate_email(to_email)
        
        # Configuration du serveur SMTP (exemple avec Gmail)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("alexevrance0@gmail.com", "0000")  # Remplacer par tes identifiants
        
        msg = MIMEMultipart()
        msg['From'] = 'your_email@gmail.com'
        msg['To'] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        print(f'Email envoyé à {to_email}')
        
        server.quit()
    except EmailNotValidError as e:
        print(f"Email invalide : {e}")
    except Exception as e:
        print(f"Erreur en envoyant l'email : {e}")

# Alertes Automatisées (Exemple simple basé sur l'analyse des cotes)
def check_odds_alert(cote_team_a, cote_team_b):
    """
    Vérifie les anomalies de cotes (exemple basé sur une condition fictive)
    """
    if cote_team_a > cote_team_b:
        send_push_notification(
            "Anomalie détectée : Cote inverse",
            f"La cote de l’équipe A est plus élevée que celle de l’équipe B alors que la majorité des paris sont sur l’équipe B.",
            "user_device_token"
        )
        send_email(
            "Anomalie de cotes détectée",
            f"Une anomalie a été détectée dans les cotes : l’équipe A a une cote plus élevée malgré des mises majoritaires sur l’équipe B.",
            "user_email@example.com"
        )

# Fonction principale pour envoyer des alertes diverses
def main():
    """
    Fonction principale qui gère l'envoi de notifications push et emails selon les événements.
    """
    init_fcm()  # Initialisation de FCM
    
    # Notifications de tests
    send_push_notification(
        "Prédiction du jour", 
        "La probabilité de victoire de l'équipe X est supérieure à 85%.", 
        "user_device_token"
    )
    
    send_email(
        "Récapitulatif des prédictions",
        "Voici les prédictions du jour pour les matchs en Asie...",
        "user_email@example.com"
    )

    # Simuler un changement dans les cotes pour tester les alertes
    cote_team_a = random.uniform(1.5, 3.0)  # Cote aléatoire entre 1.5 et 3.0
    cote_team_b = random.uniform(1.5, 3.0)  # Cote aléatoire entre 1.5 et 3.0

    print(f"Vérification des cotes : Team A - {cote_team_a}, Team B - {cote_team_b}")
    
    check_odds_alert(cote_team_a, cote_team_b)  # Vérifier si l'alerte doit être envoyée

if __name__ == "__main__":
    main()

