# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->
fix go lower go higher hint after submitting guess

| | Model A | Model B |
|-|---------|---------|
| **Model name** |Claude |ChatGPT |
| **Response summary** |Found 2 bugs producing wrong hints. Inverted message in app.py:32-48, reversed it. And, string coercion on even attempts in app.py:159-162. Every other guess converted the secret to a string before comparing. Removed it, and on check_guess, normalized both sides with int(). |Two problems, one is in check_guess(), and the other one is in the section that intentionally changing secret between an integer and a string before calling check_guess(). So reversion the hint message for guess > secret and guess < secret in check_guess() function. And on calling check_guess, directly pass in the secret session variable which is an int.|
| **More Pythonic?** |The same |The same |
| **Clearer explanation?** |Easy to understand |Easier to understand |

**Which did you prefer and why?**  
<!-- Your conclusion -->
I prefer ChatGPT. It gives explanation in between changes, and more precise. So I understand each change before I apply it to the code file.  Claude gives the explanation at the end after I accepted the changes and tests. So I have to analyze the code myself to see if it makes sense and whether to accept or reject the fix, even though I can revert or modify the code again later.