# Game Theory Strategies

This project implements various game theory strategies for iterated games. The strategies are designed to interact with each other over multiple rounds, and their performance is evaluated based on the scores they accumulate.

## Strategies

- **Grudger (LeChat, ChatGPT)**: Cooperates until the opponent defects, then always defects.
- **Pavlov (LeChat, Claude, ChatGPT)**: Repeats the previous move if the outcome was good, otherwise switches.
- **Forgiving Tit for Tat (Deepseek, ChatGPT)**: Mimics the opponent but occasionally forgives defections.
- **Tit for Tat**: Mimics the opponent's previous move.
- **Always Decline**: Always defects.
- **Always Accept**: Always cooperates.
- **Majority (ChatGPT)**: Chooses the opponent's most frequent move.
- **Adaptive Strategy (Deepseek)**: Cooperates if the opponent's acceptance rate is 50% or higher.
- **Soft Majority (LeChat)**: Cooperates if acceptances are more than 50%.
- **Hard Majority (LeChat)**: Defects if declines are more than 50%.
- **Periodic Cooperator (LeChat)**: Alternates between cooperation and defection.
- **Gradual Forgiveness (Claude)**: Punishes defection but gradually returns to cooperation.
- **Pattern Detector (Claude)**: Detects patterns in the opponent's play and adjusts accordingly.

## Running the Game

The `run_game` function simulates a game between two strategies over a specified number of rounds. The scores are accumulated and used to rank the strategies.

## Example Usage

```python
from collections import defaultdict
import random

# Define strategies and run the game
strategies = {
    "Grudger (LeChat, ChatGPT)": grudger,
    "Pavlov (LeChat, Claude, ChatGPT)": pavlov,
    // ...existing code...
}

scores = defaultdict(int)

for name1, strat1 in strategies.items():
    for name2, strat2 in strategies.items():
        rounds = random.randint(200, 1000)
        score1, score2 = run_game(strat1, strat2, rounds)
        scores[name1] += score1
        scores[name2] += score2

sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

print("Final Rankings:")
for rank, (name, score) in enumerate(sorted_scores, 1):
    print(f"{rank}. {name}: {score} points")
```

This will output the final rankings of the strategies based on their accumulated scores.
