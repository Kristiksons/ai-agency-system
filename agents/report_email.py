def build_email_report(schedule, stats, revenue):

    text = "WEEKLY CONTENT REPORT\n\n"

    text += f"Avg Score: {stats['avg_score']}\n"
    text += f"Best Day: {stats['best_day']}\n"
    text += f"Estimated Leads: {revenue['total_leads']}\n"
    text += f"Estimated Revenue: ${revenue['estimated_revenue']}\n\n"

    text += "CONTENT:\n\n"

    i = 0
    while i < len(schedule):

        item = schedule[i]

        text += f"""
DAY: {item['day']}
IDEA: {item['post']['idea']}
CTA: {item['post']['cta']}

-------------------
"""

        i += 1

    return text
