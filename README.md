# Projeckt_Pythons.09
Projektstruktur
project/
│
├── app.py                     # Hauptdatei, die den Server startet
├── HttpHandler.py             # Verarbeitet HTTP-Anfragen und API-Endpunkte
├── User.py                    # Repräsentiert die Benutzerdaten
├── Response.py                # Hilfsklasse für API-Antworten
├── FormatCheck.py             # Überprüft die Eingabedaten
├── JWTManger.py               # Verwaltet JWT-Token für die Authentifizierung
├── interfaces/
│   ├── IController.py         # Abstrakte Schnittstelle für Controller
│   └── IModel.py              # Abstrakte Schnittstelle für Modelle
├── models/
│   ├── UserModel.py           # Implementiert die Benutzerlogik (IModel)
│   └── DBConnection.py        # Verbindung zur Datenbank
├── database/
│   ├── DBMigrate.py           # Verwaltet Datenbankmigrationen
│   └── USERTable.py           # Spezifische Logik für die Benutzertabelle
└── README.md                  # Projektbeschreibung und Anleitung