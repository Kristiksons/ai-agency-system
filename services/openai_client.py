import random


def generate(prompt):

    niche = "business"

    if "niche:" in prompt.lower():
        try:
            niche = prompt.lower().split("niche:")[1].split("\n")[0].strip()
        except:
            pass

    content_types = [
        "viral",
        "educational",
        "storytelling",
        "controversial",
        "authority",
        "engagement",
        "sales"
    ]

    hooks = {
        "viral": [
            f"The biggest mistake in {niche}",
            f"Nobody talks about this in {niche}",
            f"This is why most people fail in {niche}"
        ],
        "educational": [
            f"3 things every {niche} business should know",
            f"The beginner guide to {niche}",
            f"How successful people approach {niche}"
        ],
        "storytelling": [
            f"A client completely changed their results with this",
            f"How one small change transformed a business",
            f"The lesson we learned the hard way"
        ],
        "controversial": [
            f"Unpopular opinion about {niche}",
            f"Most experts are wrong about this",
            f"Stop following this common advice"
        ],
        "authority": [
            f"What years of experience taught us",
            f"The framework professionals actually use",
            f"The strategy behind consistent results"
        ],
        "engagement": [
            f"What's your biggest challenge with {niche}?",
            f"Agree or disagree?",
            f"We want your opinion on this"
        ],
        "sales": [
            f"Ready to improve your {niche} results?",
            f"Here's how we can help",
            f"Let's solve your biggest problem"
        ]
    }

    captions = {
        "viral": f"Most people never realize this until it's too late in {niche}.",
        "educational": f"Here's a practical lesson you can apply today.",
        "storytelling": f"This real story contains an important lesson.",
        "controversial": f"You may disagree, but here's our perspective.",
        "authority": f"This comes from real experience and testing.",
        "engagement": f"Drop your answer in the comments.",
        "sales": f"If you want faster results, let's talk."
    }

    why_it_works = {
        "viral": "Strong curiosity creates higher watch time.",
        "educational": "Educational content gets saved frequently.",
        "storytelling": "Stories increase audience connection.",
        "controversial": "Controversy drives comments and discussion.",
        "authority": "Authority content builds trust.",
        "engagement": "Questions increase interaction.",
        "sales": "Strong CTA can generate leads."
    }

    posting_times = [
        "7:00 AM",
        "12:00 PM",
        "6:00 PM",
        "8:00 PM"
    ]

    result = ""

    i = 0
    while i < len(content_types):

        content_type = content_types[i]

        result += f"""
Day {i + 1}:
Hook: {random.choice(hooks[content_type])}
Caption: {captions[content_type]}
Hashtags: #{niche.replace(' ', '')} #marketing #growth #business #content
Reel Script: Hook -> Value -> CTA
Best Time: {random.choice(posting_times)}
Why it works: {why_it_works[content_type]}
"""

        i += 1

    return result