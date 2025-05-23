import pytest
from datetime import datetime
import sys, os
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(__file__, os.pardir, os.pardir)
    )
)

from storage import DateTimeEventStore

def test_store_and_get_events_empty():
    store = DateTimeEventStore()
    assert store.get_events(datetime(2025,1,1), datetime(2025,12,31)) == []

def test_event_within_range():
    store = DateTimeEventStore()
    t = datetime(2025,6,15,14,0)
    store.store_event(at=t, data="Event")
    assert store.get_events(datetime(2025,6,15), datetime(2025,6,15,23,59)) == ["Event"]

def test_event_outside_range():
    store = DateTimeEventStore()
    t = datetime(2025,6,15,14,0)
    store.store_event(at=t, data="Event")
    assert store.get_events(datetime(2025,6,16), datetime(2025,6,16,23,59)) == []

def test_multiple_events_order():
    store = DateTimeEventStore()
    t1 = datetime(2025,1,1,10,0)
    t2 = datetime(2025,1,1,9,0)
    store.store_event(at=t1, data="Second")
    store.store_event(at=t2, data="First")
    assert store.get_events(datetime(2025,1,1), datetime(2025,1,1,23,59)) == ["First", "Second"]

