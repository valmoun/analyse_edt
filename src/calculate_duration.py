"""
Module de calcul de durée d'événements pour l'analyse d'emploi du temps.

Ce module fournit une fonction principale, calculate_duration, qui permet de calculer la durée en
minutes d'un événement à partir de ses dates et heures de début et de fin, ou de retourner une
durée standard pour une journée entière. 

Fonctionnalités :
- Calcul de la durée en minutes entre deux dates/heures.
- Prise en charge des événements couvrant une journée entière (retourne 7 heures par défaut).
- Exemples d'utilisation inclus en fin de module.

Auteur : Valentin Mounier
Version : 0.1.0
"""

from datetime import datetime

def calculate_duration(start_day, end_day, start_time, end_time, journee_entiere):
    """
    Calcule la durée d'un évènement en minutes.
    - start_day, end_day : pandas.Timestamp
    - start_time, end_time : datetime.time
    - journee_entiere : bool
    """
    if journee_entiere:
        return 7 * 60  # 7 heures en minutes

    # Combine date and time
    start_dt = datetime.combine(start_day, start_time)
    end_dt = datetime.combine(end_day, end_time)
    duration = end_dt - start_dt
    return int(duration.total_seconds() // 60)

# Exemple d'utilisation :
if __name__ == "__main__":
    # Exemple 1 : Journée entière
    print(calculate_duration("2024-06-01", "2024-06-01", "09:00:00", "17:00:00", True))  # 420

    # Exemple 2 : Evènement ponctuel
    print(calculate_duration("2024-06-01", "2024-06-01", "09:00:00", "12:30:00", False))  # 210
