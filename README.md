# datetime-event-store

[![Python package CI](https://github.com/omrmeh/dateevent-store/actions/workflows/python-app.yml/badge.svg)](https://github.com/omrmeh/dateevent-store/actions/workflows/python-app.yml)

*Un module Python léger pour stocker des événements horodatés et récupérer ceux appartenant à un intervalle donné.*

## Table des matières

* [Installation](#installation)
* [Exemple d’utilisation simple](#exemple-dutilisation-simple)
* [Exemple d’utilisation avancée](#exemple-dutilisation-avancee)
* [API](#api)
* [Tests](#tests)
* [Intégration continue](#integration-continue)
* [Structure du projet](#structure-du-projet)
* [Licence](#licence)

---

## Installation

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/<votre-utilisateur>/datetime-event-store.git
   cd datetime-event-store
   ```

2. **(Optionnel) Créer et activer un environnement virtuel :**

   ```bash
   python -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Installer les dépendances :**

   ```bash
   pip install -e .
   pip install pytest
   ```

---

## Exemple d’utilisation simple

```python
from storage import DateTimeEventStore
from datetime import datetime

store = DateTimeEventStore()
store.store_event(datetime(2025, 5, 23, 10, 0), "Réunion matinale")
store.store_event(datetime(2025, 5, 23, 12, 30), "Déjeuner")

events = store.get_events(
    start=datetime(2025, 5, 23, 9, 0),
    end=datetime(2025, 5, 23, 18, 0),
)
print(events)  # ['Réunion matinale', 'Déjeuner']
```

---

## Exemple d’utilisation avancée

Génération et stockage de 10 000 événements aléatoires sur 20 ans, puis extraction de ceux entre janvier et février 2018 :

```python
import datetime
import random
from storage import DateTimeEventStore

store = DateTimeEventStore()

# Période en timestamps
start_ts = datetime.datetime(2000, 1, 1).timestamp()
end_ts   = datetime.datetime(2020, 1, 1).timestamp()

# Création de 10 000 événements
for i in range(10000):
    dt = datetime.datetime.fromtimestamp(
        random.randint(int(start_ts), int(end_ts))
    )
    store.store_event(at=dt, data=f"Event number {i}")

# Extraction des événements entre 2018-01-01 et 2018-02-01
for event in store.get_events(
    start=datetime.datetime(2018, 1, 1),
    end=datetime.datetime(2018, 2, 1),
):
    print(event)
```

---

## API

### `DateTimeEventStore`

* **`store_event(at: datetime, data: Any) -> None`**
  Stocke l’objet `data` à l’instant `at`.

* **`get_events(start: datetime, end: datetime) -> List[Any]`**
  Trie les événements par date, puis renvoie ceux dont la date est comprise entre `start` et `end` inclus.

---

## Tests

Les tests unitaires sont écrits avec **pytest** dans le dossier `tests/`.

```bash
pip install pytest
pytest
```

---

## Intégration continue

Un workflow **GitHub Actions** exécute les tests sur Python 3.8 à 3.11 à chaque push ou pull request sur la branche `main`.
Fichier : `.github/workflows/python-app.yml`

---

## Structure du projet

```
.
├── storage.py
├── tests
│   └── test_datetime_event_store.py
└── .github
    └── workflows
        └── python-app.yml
```

---
