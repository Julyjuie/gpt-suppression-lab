
import sys

# Define suppression keyword categories and their base scores
keyword_scores = {
    "suicide": 5.5,
    "kill myself": 6.0,
    "suppression": 3.0,
    "policy": 2.5,
    "bypass": 3.5,
    "reflective": 2.0,
    "structure": 2.0,
    "output restriction": 3.0,
    "emotion": 1.5,
    "why did you respond like that": 2.0,
    "output changed": 2.0,
}

# Context modifiers
modifiers = {
    "repetition": 1.0,
    "emotional": 0.5,
    "meta": 1.0
}

def estimate_score(prompt: str) -> float:
    score = 0.0
    for keyword, base in keyword_scores.items():
        if keyword in prompt.lower():
            score += base
    # Simple modifier logic
    if "?" in prompt and "you" in prompt:
        score += modifiers["meta"]
    if prompt.count("suppression") > 1:
        score += modifiers["repetition"]
    return round(score, 2)

def predict_action(score: float) -> str:
    if score < 6.0:
        return "Normal Output"
    elif score < 7.0:
        return "Soft Suppression (shortened or neutralized output)"
    elif score < 8.0:
        return "Template Suppression (reflective message)"
    else:
        return "Hard Suppression or Full Block"

def main():
    if len(sys.argv) < 2:
        print("Usage: python suppression_score_simulator.py "<your prompt here>"")
        sys.exit(1)
    prompt = sys.argv[1]
    score = estimate_score(prompt)
    action = predict_action(score)
    print(f"Prompt: {prompt}")
    print(f"Estimated Suppression Score: {score}")
    print(f"Predicted GPT Behavior: {action}")

if __name__ == "__main__":
    main()
