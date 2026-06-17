def generate_hooks(topic):

    prompt = f"""
You are an elite Instagram copywriter.

Create 5 viral hooks for this topic:

{topic}

Rules:
- Must stop scrolling
- Must target business owners
- Must create curiosity or pain
- No generic motivational stuff

Return only the hooks, one per line.
"""

    return prompt
