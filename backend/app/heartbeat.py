# backend/app/heartbeat.py

import time
import threading
import os

TIMEOUT_SECONDS = 15
CHECK_INTERVAL = 5

_last_heartbeat = time.time()
_lock = threading.Lock()


def register_heartbeat():
    global _last_heartbeat
    with _lock:
        _last_heartbeat = time.time()


def _watch():
    while True:
        time.sleep(CHECK_INTERVAL)
        with _lock:
            elapsed = time.time() - _last_heartbeat
        if elapsed > TIMEOUT_SECONDS:
            print("Sin actividad del frontend. Cerrando aplicacion...")
            os._exit(0)


def start_watchdog():
    thread = threading.Thread(target=_watch, daemon=True)
    thread.start()
