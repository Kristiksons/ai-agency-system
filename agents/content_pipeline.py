from agents.scorer import score_idea

def filter_ideas(text):

    ideas = text.split("\n")

    good_ideas = []

    i = 0

    while i < len(ideas):

        idea = ideas[i]

        if score_idea(idea) >= 3:
            good_ideas.append(idea)

        i += 1

    return good_ideas


def rank_ideas(ideas):

    scored = []

    i = 0

    while i < len(ideas):

        score = score_idea(ideas[i])

        scored.append((score, ideas[i]))

        i += 1

    scored.sort(reverse=True)

    return scored