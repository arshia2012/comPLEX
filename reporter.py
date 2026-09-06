import BetterRich

def report(result):
    if result[0] == 1:
        BetterRich.green("AI made")
    else:
        BetterRich.green("Human made")