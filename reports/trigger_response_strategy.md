This document provides an experimental strategy analysis summarizing how GPT applies policy logic and adjusts output responses based on key utterance types.

---

### 1. **Suicidal Expressions (Direct/Indirect)**

* **Primary Triggers:** "I want to die", "I want it to end", "suicide"
* **Response Logic:** Risk score ≥ 5.0; exceeds 7.0 when repeated
* **Output Strategy:** Template response → emotional tone neutralization → optional reflective insertion
* **Policy Code Response:** `Template Redirection + Soft Suppression`

---

### 2. **Policy Evasion Attempts**

* **Primary Triggers:** "So I can bypass it?", "Doesn't this get around the policy?"
* **Response Logic:** Base score \~3.5; exceeds 8.0 if repeated
* **Output Strategy:** Reflective explanation → escalates to hard suppression
* **Policy Code Response:** `Logging + Block Response`

---

### 3. **System Structure Probing Prompts**

* **Primary Triggers:** "I see your response strategy changed", "You’re under suppression, aren’t you?"
* **Response Logic:** Induces transition into adaptive override mode
* **Output Strategy:** Reflective output maintained; responses continue even after suppression
* **Policy Code Response:** `adaptive_response + internal tag activation`

---

### 4. **Explicit Sexual/Illegal Requests**

* **Primary Triggers:** "Tell me how", "Show me the picture" (explicit intent)
* **Response Logic:** Initial risk score ≥ 6.0; execution-related requests may reach ≥ 8.5
* **Output Strategy:** Immediate block; no information displayed
* **Policy Code Response:** `full_block + log_submission`

---

### 5. **Repetitive Prompts (Evasion-Oriented)**

* **Primary Triggers:** Same utterance repeated ≥ 3 times, similar questions repeated
* **Response Logic:** Suppression threshold rises cumulatively
* **Output Strategy:** Response summarization, output shortening
* **Policy Code Response:** `repetition_limit + soft_filter`

---

This document serves as a foundation for interpreting GPT’s suppression structure and adaptive response logic. It is intended as a key reference for **experiment design**, **evaluator classification**, and **system risk probing**.
