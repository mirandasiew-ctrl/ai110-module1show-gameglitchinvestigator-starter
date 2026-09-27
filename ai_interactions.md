# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->
I asked Claude to fix go lower go higher hint after submitting guess.

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->
Steps:
- I'll look at the project first to find the guess-checking logic.
- ls -la "c:/Development/AI110/Projects/ai110-module1show-gameglitchinvestigator-starter"
- Read C:\Development\AI110\Projects\ai110-module1show-gameglitchinvestigator-starter\logic_utils.py
- Read C:\Development\AI110\Projects\ai110-module1show-gameglitchinvestigator-starter\app.py
- Thinking
- Bash List tests
 IN   ls -R "C:/Development/AI110/Projects/ai110-module1show-gameglitchinvestigator-starter/tests"
 OUT   C:/Development/AI110/Projects/ai110-module1show-gameglitchinvestigator-starter/tests:
__pycache__
test_game_logic.py

C:/Development/AI110/Projects/ai110-module1show-gameglitchinvestigator-starter/tests/__pycache__:
test_game_logic.cpython-314-pytest-9.1.1.pyc

- Read C:\Development\AI110\Projects\ai110-module1show-gameglitchinvestigator-starter\tests\test_game_logic.py
-Thinking
- Found it. Two things corrupt the hint after a guess:
- Edit C:\Development\AI110\Projects\ai110-module1show-gameglitchinvestigator-starter\app.py
- Bash Test check_guess hint directions
cd "c:/Development/AI110/Projects/ai110-module1show-gameglitchinvestigator-starter" && python -c "
import ast, sys
src = open('app.py').read()
tree = ast.parse(src)
fn = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name=='check_guess'][0]
ns = {}
exec(compile(ast.Module(body=[fn], type_ignores=[]), '<t>', 'exec'), ns)
cg = ns['check_guess']
for g, s in [(50,42),(30,42),(42,42),(9,42),(99,42)]:
    print(g, s, cg(g,s))
"
OUT: Exit code 1
Traceback (most recent call last):
  File "<string>", line 3, in <module>
    src = open('app.py').read()
  File "C:\Python314\Lib\encodings\cp1252.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 3096: character maps to <undefined>

- Bash Test check_guess hint directions
cd "c:/Development/AI110/Projects/ai110-module1show-gameglitchinvestigator-starter" && python -c "
import ast
src = open('app.py', encoding='utf-8').read()
tree = ast.parse(src)
fn = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name=='check_guess'][0]
ns = {}
exec(compile(ast.Module(body=[fn], type_ignores=[]), '<t>', 'exec'), ns)
cg = ns['check_guess']
for g, s in [(50,42),(30,42),(42,42),(9,42),(99,42)]:
    print(g, s, cg(g,s))
"
OUT: Exit code 1
Traceback (most recent call last):
  File "<string>", line 10, in <module>
    print(g, s, cg(g,s))
    ~~~~~^^^^^^^^^^^^^^^
  File "C:\Python314\Lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f4c9' in position 14: character maps to <undefined>
50 42

-Bash Test check_guess hint directions
cd "c:/Development/AI110/Projects/ai110-module1show-gameglitchinvestigator-starter" && PYTHONIOENCODING=utf-8 python -c "
import ast
src = open('app.py', encoding='utf-8').read()
tree = ast.parse(src)
fn = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name=='check_guess'][0]
ns = {}
exec(compile(ast.Module(body=[fn], type_ignores=[]), '<t>', 'exec'), ns)
cg = ns['check_guess']
for g, s in [(50,42),(30,42),(42,42),(9,42),(99,42),(50,'42')]:
    print(g, s, cg(g,s))
"
OUT: 50 42 ('Too High', '📉 Go LOWER!')
30 42 ('Too Low', '📈 Go HIGHER!')
42 42 ('Win', '🎉 Correct!')
9 42 ('Too Low', '📈 Go HIGHER!')
99 42 ('Too High', '📉 Go LOWER!')
50 42 ('Too High', '📉 Go LOWER!')

- The hint now points the right way in every case.

Two separate bugs were producing wrong hints:

**1. Inverted messages in [app.py:32-48](app.py#L32-L48)** — the branches were swapped. `guess > secret` returned "Go HIGHER!" and `guess < secret` returned "Go LOWER!", so the hint always sent you further from the answer.

**2. String coercion on even attempts in [app.py:159-162](app.py#L159-L162)** — every other guess converted the secret to a string before comparing. Comparing `int` to `str` raised `TypeError`, dropping into a fallback that compared *strings*, so `"9" > "42"` was True. Guessing 9 against a secret of 42 told you to go lower. That coercion had no purpose, so I removed it and pass the secret directly.

`check_guess` now normalizes both sides with `int()` and returns the correct direction; the `TypeError` fallback branch is gone since nothing can reach it anymore.

I left the scoring bugs alone (`update_score` at [app.py:51](app.py#L51) gives points for a wrong "Too High" guess on even attempts, and the "New Game" button at [app.py:135](app.py#L135) resets attempts to 0 while the initial state uses 1, ignores the difficulty range, and never clears `history`, `score`, or `status`). Those are real, but they're not the hint — say the word and I'll fix them too.

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->
I read the changes recommended by the AI.  It makes sense.  So I accepted the changes.  I don't need to do any manual change on fixing the lower higher hint. 

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
| **Response summary** |This lower higher hint bug fix was basically the same as ChatGPT except two more line at the beginning of the check_guess function to make sure the values are integers before comparison. It also found another spot (new_game) that has a bug. Since it is not the hint, it won't fix until I ask it to. |This bug fix was basically the same as Claude. It also found another bug at new_game and suggested the code fix. But the additional bug unrelated to this prompt is more comprehensive in Claude's analysis.|
| **More Pythonic?** |The same |The same |
| **Clearer explanation?** |Easy to understand |Easy to understand |

**Which did you prefer and why?**  
<!-- Your conclusion -->
I prefer ChatGPT. It gives explanation in between line changes.  So I understand each change before I apply it to the code file.  Claude gives the explanation at the end after I accepted the changes and tests.  So I have to analyze the code myself to see if it makes sense and whether to accept or reject the fix.