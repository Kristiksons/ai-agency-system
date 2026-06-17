import subprocess


def generate(prompt):

    try:
        result = subprocess.run(
            ["ollama", "run", "llama3.1:latest", prompt],
            capture_output=True,
            text=True,
            timeout=20  # 🔥 IMPORTANT: prevents freezing forever
        )

        output = result.stdout.strip()

        if output:
            return output

    except Exception as e:
        print("OLLAMA FAILED:", e)

    # fallback ALWAYS
    return """
Day 1: Hook → Client transformation breakdown
Day 2: Hook → Common mistake in niche
Day 3: Hook → Quick win strategy
Day 4: Hook → Behind the scenes process
Day 5: Hook → Authority building post
Day 6: Hook → Engagement question
Day 7: Hook → Offer / CTA post
"""