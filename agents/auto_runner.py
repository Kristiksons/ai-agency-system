import time

from agents.clients import get_clients
from agents.calendar import create_calendar
from agents.scheduler import build_schedule
from agents.storage import save_run
from agents.analytics import analyze_history
from agents.revenue import estimate_value
from agents.reports import generate_pdf


def run_weekly_job():

    clients = get_clients()

    i = 0
    while i < len(clients):

        client = clients[i]

        print("Running for:", client["name"])

        calendar = create_calendar(client)
        schedule = build_schedule(calendar)

        save_run(client["name"], schedule)

        stats = analyze_history([schedule])
        revenue = estimate_value(schedule)

        generate_pdf(client["name"], schedule, stats)

        print("Done:", client["name"])

        i += 1


def start_scheduler():

    while True:

        print("⏳ Running weekly AI agency job...")

        run_weekly_job()

        print("😴 Sleeping for 7 days...")

        time.sleep(60 * 60 * 24 * 7)
