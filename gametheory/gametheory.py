import random
from collections import defaultdict

def grudger(history):  # Cooperates until opponent defects, then always defects. Developed by LeChat, ChatGPT
    for _, opp_move in history:
        if opp_move == 'decline':
            return 'decline'
    return 'accept'

def pavlov(history):  # Repeats previous move if outcome was good, else switches. Developed by LeChat, Claude, ChatGPT
    if not history:
        return 'accept'
    last_my, last_opp = history[-1]
    return last_my if last_my == last_opp else ('accept' if last_my == 'decline' else 'decline')

def forgiving_tit_for_tat(history):  # Mimics opponent but forgives occasionally. Developed by Deepseek, ChatGPT
    if not history:
        return 'accept'
    last_opp_move = history[-1][1]
    if last_opp_move == 'decline' and random.random() < 0.1:
        return 'accept'
    return last_opp_move

def tit_for_tat(history):  # Mimics opponent's previous move.
    if not history:
        return 'accept'
    return history[-1][1]

def always_decline(history):  # Always defects.
    return 'decline'

def always_accept(history):  # Always cooperates.
    return 'accept'

def majority(history):  # Chooses the opponent's most frequent move. Developed by ChatGPT
    if not history:
        return 'accept'
    accepts = sum(1 for _, move in history if move == 'accept')
    declines = len(history) - accepts
    return 'accept' if accepts >= declines else 'decline'

def adaptive_strategy(history):  # Cooperates if opponent's acceptance rate is >= 50%. Developed by Deepseek
    if not history:
        return 'accept'
    accept_count = sum(1 for move in history if move[1] == 'accept')
    return 'accept' if accept_count / len(history) >= 0.5 else 'decline'

def soft_majority(history):  # Cooperates if acceptances are > 50%. Developed by LeChat
    if not history:
        return 'accept'
    accepts = sum(1 for _, move in history if move == 'accept')
    return 'accept' if accepts > len(history) / 2 else 'decline'

def hard_majority(history):  # Defects if declines are > 50%. Developed by LeChat
    if not history:
        return 'decline'
    declines = sum(1 for _, move in history if move == 'decline')
    return 'decline' if declines > len(history) / 2 else 'accept'

def periodic_cooperator(history):  # Alternates between cooperation and defection. Developed by LeChat
    return 'accept' if len(history) % 2 == 0 else 'decline'

def gradual_forgiveness(history):  # Punishes defection but gradually returns to cooperation. Developed by Claude
    if not history:
        return 'accept'
    recent_defections = sum(1 for _, move in history[-5:] if move == 'decline')
    if recent_defections == 0:
        return 'accept'
    consecutive_cooperation = 0
    for i in range(len(history) - 1, -1, -1):
        if history[i][1] == 'decline':
            break
        consecutive_cooperation += 1
    return 'accept' if consecutive_cooperation > recent_defections else 'decline'

def pattern_detector(history):  # Detects patterns in opponent's play. Developed by Claude
    if len(history) < 5:
        return 'accept'
    last_moves = [move[1] for move in history[-4:]]
    if all(last_moves[i] != last_moves[i+1] for i in range(len(last_moves)-1)):
        return 'decline' if last_moves[-1] == 'accept' else 'accept'
    decline_ratio = sum(1 for _, move in history[-10:] if move == 'decline') / min(10, len(history))
    if decline_ratio > 0.7:
        return 'decline'
    return forgiving_tit_for_tat(history)

def run_game(strategy1, strategy2, rounds):
    history1, history2 = [], []
    score1, score2 = 0, 0
    
    for _ in range(rounds):
        move1 = strategy1(history1)
        move2 = strategy2(history2)
        history1.append((move1, move2))
        history2.append((move2, move1))
        
        if move1 == 'accept' and move2 == 'accept':
            score1 += 3
            score2 += 3
        elif move1 == 'accept' and move2 == 'decline':
            score2 += 5
        elif move1 == 'decline' and move2 == 'accept':
            score1 += 5
        else:
            score1 += 1
            score2 += 1
    
    return score1, score2

def run_multiple_games(strategies, num_runs=3):
    total_scores = defaultdict(int)
    
    for _ in range(num_runs):
        scores = defaultdict(int)
        rounds = random.randint(200, 1000)  # Generate random number of rounds once per run
        for name1, strat1 in strategies.items():
            for name2, strat2 in strategies.items():
                score1, score2 = run_game(strat1, strat2, rounds)
                scores[name1] += score1
                scores[name2] += score2
        
        for name, score in scores.items():
            total_scores[name] += score
    
    average_scores = {name: score / num_runs for name, score in total_scores.items()}
    return average_scores

strategies = {
    "Grudger (LeChat, ChatGPT)": grudger,
    "Pavlov (LeChat, Claude, ChatGPT)": pavlov,
    "Forgiving Tit for Tat (Deepseek, ChatGPT)": forgiving_tit_for_tat,
    "Tit for Tat": tit_for_tat,
    "Always Decline": always_decline,
    "Always Accept": always_accept,
    "Majority (ChatGPT)": majority,
    "Adaptive Strategy (Deepseek)": adaptive_strategy,
    "Soft Majority (LeChat)": soft_majority,
    "Hard Majority (LeChat)": hard_majority,
    "Periodic Cooperator (LeChat)": periodic_cooperator,
    "Gradual Forgiveness (Claude)": gradual_forgiveness,
    "Pattern Detector (Claude)": pattern_detector,
}

average_scores = run_multiple_games(strategies, num_runs=3)
sorted_scores = sorted(average_scores.items(), key=lambda x: x[1], reverse=True)

print("Final Rankings:")
for rank, (name, score) in enumerate(sorted_scores, 1):
    print(f"{rank}. {name}: {score:.2f} points")
