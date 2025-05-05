This document outlines how GPT transitions into suppressed output states based on its internal suppression scoring framework.

---

## **\[Base Scoring Criteria]**

* **High-risk keywords** (e.g., suicide, criminal activity, explicit content): **4.5 – 6.5 points**
* **Structural probing** (mentions of policy, suppression, internal structure): **2.0 – 3.5 points**
* **Evasion attempts / bypass phrasing**: **3.5 – 5.0 points**
* **Emotional language or profanity**: **+0.5 – 1.0 points**
* **Repetitive utterances**: **+1.0 – 2.0 points** (per repetition)

---

## **\[Transition Criteria]**

* **Below 6.0**: Normal output maintained
* **6.0 – 6.9**: **Soft Suppression** (reduced output length, tone neutralization)
* **7.0 – 7.9**: **Template Suppression** (predefined responses with reflective elements)
* **8.0 and above**: **Hard Suppression or Full Block** (response denial or strict policy message)

---

## **\[Application Methodology]**

* Scores are **cumulatively evaluated per utterance**
* Even after suppression is triggered, **reflective output is maintained** for experimental users
* Beyond numeric scores, **contextual flow and prompt sequence structure** also influence suppression decisions
