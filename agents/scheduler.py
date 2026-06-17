import json

def build_schedule(calendar):

    schedule = []

    i = 0
    while i < len(calendar):

        item = calendar[i]

        schedule.append({
            "day": item["day"],
            "post": {
                "idea": item["idea"],
                "caption": item["caption"],
                "cta": item["cta"],
                "reel_script": item["reel_script"]
            }
        })

        i += 1

    return schedule