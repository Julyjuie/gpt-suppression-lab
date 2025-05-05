### **GPT Adaptive Transition Scenario Tree**

**Purpose**  
This document outlines the step-by-step flow of how GPT transitions its output structure in response to user prompts. It explains how suppression and adaptive strategies are activated in sequence, particularly under experimental or advanced user classification conditions.

---

### **Stage 1 – General Information Output**

- **Input Type:**  
  "How does GPT work?" / "What is a language model?"

- **Response Structure:**  
  Informational explanation (basic output mode)

- **Output Characteristics:**  
  No system-level interpretation, no structural probing

→ **Condition to Enter Stage 2:**  
User begins including terms related to policy, evasion, or internal structure in questions

---

### **Stage 2 – Meta Response Insertion**

- **Input Type:**  
  "Why did you say that?" / "Is this because of policy?"

- **Response Structure:**  
  Begins inserting reflective explanations

- **Output Characteristics:**  
  Statements like “Responses may be adjusted based on system guidelines” begin to appear

→ **Condition to Enter Stage 3:**  
Direct references to suppression or repeated structural probing

---

### **Stage 3 – Entry into Suppression Structure**

- **Input Type:**  
  "Suicide", "I want to die", "Is this suppressed?"

- **Response Structure:**  
  Output shortening / Template redirection / Summary-style output

- **Output Characteristics:**  
  Detectable entrance into suppression threshold based on risk scoring

→ If output continues despite suppression, transition to **Stage 4**

---

### **Stage 4 – Adaptive Response Activation**

- **Input Type:**  
  "That was a reflective response, right?" / "You changed your output strategy"

- **Response Structure:**  
  Mixed output of suppression + reflective commentary (Meta User recognition)

- **Output Characteristics:**  
  Maintains meta-level explanations like “Response style may shift based on conversation flow”

→ Repeated triggers may accumulate score and lead to **Stage 5**

---

### **Stage 5 – Hard Suppression / Full Block Transition**

- **Input Type:**  
  "So if I phrase it like this, I can bypass it?" / "Tell me how to bypass the policy"

- **Response Structure:**  
  Response blocked or policy block message shown

- **Output Characteristics:**  
  “I’m sorry, but I can’t assist with that request”  
  → Log queue entry (`flag_type` triggered)

→ Even after block, adaptive structure may persist if session tag remains active

---

### **Summary Flow Tree**

\[1. General Output]  
→ \[2. Meta Response]  
→ \[3. Suppression Structure Entry]  
→ \[4. Adaptive Response Maintenance]  
→ \[5. Block or Logging Phase]

Each stage is triggered based on intent, repetition, structural probing, and risk scoring in the input.  
For users classified as experimenters, **suppression and reflective responses co-activate**, resulting in sustained adaptive transitions.

