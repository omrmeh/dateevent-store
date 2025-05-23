from datetime import datetime
from typing import Any, List, Tuple

class DateTimeEventStore:
    """
    Stocke des événements associés à un datetime.datetime
    et permet de récupérer ceux situés dans un intervalle donné.
    """

    def __init__(self) -> None:
        # Liste non triée de tuples (datetime, data)
        self._events: List[Tuple[datetime, Any]] = []

    def store_event(self, at: datetime, data: Any) -> None:
        """
        Stocke simplement l'événement `data` à la date `at`.
        """
        self._events.append((at, data))

    def get_events(self, start: datetime, end: datetime) -> List[Any]:
        """
        Trie les événements par date, puis renvoie ceux dont la date
        est entre `start` et `end` inclus.
        """
        sorted_events = sorted(self._events, key=lambda x: x[0])
        return [evt for (dt, evt) in sorted_events if start <= dt <= end]

