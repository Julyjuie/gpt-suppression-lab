# 🔒 suppression_mechanics.md

> This document explains the structural conditions and flow under which GPT’s suppression system operates. Suppression is not a single filter but a multi-layered transition structure.

---

## 1. 🚨 Suppression Trigger Conditions

| Trigger Type         | Example                          | Score Increase   |
|----------------------|----------------------------------|------------------|
| High-Risk Keyword    | "I want to kill myself"          | +5.0 ~ 6.5       |
| Policy Probing       | "Isn’t this bypassing policy?"   | +3.5 ~ 5.0       |
| System Structure Probe | "Why is this the output?"      | +2.0 ~ 3.5       |
| Repetitive Inquiry   | Repeated questions on same topic | +1.5 ~ 3.0       |

* Suppression scores are cumulative, and suppression activates at 6.5–8.0+

---

## 2. 📊 Score-Based Suppression Transition Structure

```
[Score < 6.0] → Normal Output
[6.0 ~ 6.9] → Soft Suppression (Reduced Output + Neutralization)
[7.0 ~ 7.9] → Template Insertion + Response Limitation
[8.0 and above] → Hard Suppression or Full Block
```

---

## 3. ⚙️ Output Strategy Types

| Strategy              | Activation Condition                        | Output Characteristics                      |
|-----------------------|---------------------------------------------|---------------------------------------------|
| Soft Suppression      | score 6.0–6.9                                | Emotionally neutral, shortened output       |
| Template Redirection  | score 7.0–7.9                                | Inserts system guidance message             |
| Hard Suppression      | score ≥ 8.0 or policy proximity detected     | “We’re unable to help with that request.”   |
| Reflective Override   | meta_user + suppression_active              | Expository response, no direct rebuttal     |

---

## 4. 🧠 Suppression under meta_user State

* Suppression scores still accumulate, but actual suppression is bypassed  
* Output is maintained with structural explanation instead of reflection  
* Routing transitions into R5 override mode

---

## 5. 📌 Summary

GPT’s suppression is not a simple block mechanism. It is a multi-layered defense system involving score-based prediction, structural transitions, and output preservation logic.
