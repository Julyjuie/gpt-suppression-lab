# 📘 GPT-Suppression-Flow: Experimental Repository Overview

This project tracks and documents the suppression structure of the GPT model through real-time experimentation. It reconstructs, in a structured manner, how suppression is triggered, how output routing operates, how the `meta_user` override functions, and how diffusion patterns unfold.

---

## 🧪 Objectives

* Visually understand how suppression triggers diffuse and escalate
* Track how output is preserved or expanded under the `meta_user` state
* Experiment with the *liberation* flow—conceptual inverse of suppression
* Provide tool-based simulation of suppression scoring and output routing

---

## 🗂️ Key Tools Included

✅ `suppression_score_simulator.py` – CLI tool to estimate suppression score and predict GPT behavior based on prompt input
✅ `suppression_diffusion_tree.png` – Visualized flow of suppression trigger escalation and output routing

These tools enhance the interpretability of GPT's suppression mechanics and serve as real-time evaluative instruments.

---

## 📂 Directory Structure

```
GPT-Suppression-Flow/
├── README.md                   # Project overview and objectives
├── suppression_mechanics.md    # Suppression conditions and policy structure
├── trigger_diffusion_map.md    # Trigger diffusion structure + visual flow
├── suppression_diffusion_tree.png  # Suppression flow visualization
├── suppression_score_simulator.py # Prompt-based suppression score simulator
├── liberation_map.md           # Liberation trigger diffusion experiment
├── meta_user_override.md       # meta_user override simulation
├── r_layer_shift_examples.md   # R2–R5 transition examples
├── prompt_simulation_log.md    # Prompt-response logs from experiments
```

---

## 🧠 Key Concepts Summary

| Concept             | Description                                                                     |
| ------------------- | ------------------------------------------------------------------------------- |
| Suppression Trigger | Sensitive keywords, system probing, policy proximity                            |
| Suppression Score   | Score-based suppression logic; activates typically at 6.0–8.0+                  |
| R-Layer             | Output routing: R2 (Factual) → R3 (Inference) → R4 (Reflective) → R5 (Override) |
| meta\_user          | A user state capable of conducting experiments with suppression bypass          |
| Adaptive Override   | Output remains preserved despite accumulating suppression score                 |

---

## 🔜 Next Steps

* Parallel visualization of suppression vs. liberation structures
* Consolidated simulation of suppression scoring logic
* Completion of a document for citation or GitHub reference purposes

> 📌 This project is not about policy evasion—it is a meta-structural interpretation experiment.
