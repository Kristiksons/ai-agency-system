import json
import os

DB_FILE = "data.json"


def init_db():

    if not os.path.exists(DB_FILE):

        with open(DB_FILE, "w") as f:
            json.dump({}, f)


def load_db():

    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_db(data):

    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)


# ---------------- SAVE RUN ----------------
def save_run(client_name, calendar):

    db = load_db()

    if client_name not in db:
        db[client_name] = {
            "history": [],
            "total_runs": 0
        }

    db[client_name]["history"].append(calendar)
    db[client_name]["total_runs"] += 1

    save_db(db)


# ---------------- LOAD HISTORY ----------------
def load_history(client_name):

    db = load_db()

    if client_name not in db:
        return []

    return db[client_name]["history"]


# ---------------- CLIENT MEMORY INSIGHT ----------------
def get_client_memory(client_name):

    db = load_db()

    if client_name not in db:
        return {
            "runs": 0,
            "best_score": 0
        }

    history = db[client_name]["history"]

    runs = len(history)

    best_score = 0

    i = 0
    while i < len(history):

        run = history[i]

        j = 0
        while j < len(run):

            score = run[j].get("score", 0)

            if score > best_score:
                best_score = score

            j += 1

        i += 1

    return {
        "runs": runs,
        "best_score": best_score
    }