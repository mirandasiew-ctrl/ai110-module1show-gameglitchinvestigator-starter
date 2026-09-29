# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1. The "Go LOWER!" "Go HIGHER!" hint is wrong. When I first started the game, the secret number was 53, I guessed 50, it said "Go LOWER!"

2. The New Game button doesn't work, cannot play a new game. When click New Game button, Secret was reset to a new number 35. Attempts was reset to 0. Score was reset to 10. History still showed the past guesses I submitted. The message at the bottom said "You already won. Start a new game to play again."

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Secret: 53, guessed 50 |hint: Go HIGHER! |hint: Go LOWER! |None |

|Click New Game button |Can play a new game |Nothing happens when submit a guess, and the hint keeps saying "Start a new game to play again." |None |

|When change the difficulty level |The message will be updated to reflect the number range for the difficulty level |The message always says guess a number between 1 and 100. |None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude and ChatGPT

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Two separate bugs were producing wrong hints:
1. Inverted messages in app.py:32-48 — the branches were swapped. guess > secret returned "Go HIGHER!" and guess < secret returned "Go LOWER!", so the hint always sent you further from the answer.
2. String coercion on even attempts in app.py:159-162 — every other guess converted the secret to a string before comparing. Comparing int to str raised TypeError, dropping into a fallback that compared strings, so "9" > "42" was True. Guessing 9 against a secret of 42 told you to go lower. That coercion had no purpose, so I removed it and pass the secret directly.
AI ran the test to verify the result: Bash Test check_guess hint directions
IN: cd "c:/Development/AI110/Projects/ai110-module1show-gameglitchinvestigator-starter" && PYTHONIOENCODING=utf-8 python -c "
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
I also ran the application and play the game to verify the fix is correct.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
I accepted all the AI suggestions. I compared the change in the new game initialization change between Claude and ChatGPT. ChatGPT has an addition line that Claude doesn't have and I feel it is good to have it so the game status is clearer. After accepted the Claude suggested changes to update the code, I manually added that line from ChatGPT.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Run python -m pytest
======================= test session starts =======================
platform win32 -- Python 3.14.2, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Development\AI110\Projects\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 6 items                                                  

tests\test_game_logic.py ......                              [100%]

======================== 6 passed in 0.06s ========================

Also run the application to verify manually. 
python -m streamlit run app.py

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
When I tested the high low hint fix manually by running the application, the Secret was 26, I entered 50 and submitted, the hint message said GO LOWER. When I entered 10 and submitted, the hing message said GO HIGHER. This showed the fix was correct.

- Did AI help you design or understand any tests? How?
Yes, AI helped. It has detail explanation on the problems and the changes to correct the problems. It also ran tests on the changes to showed that was correct.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit app is like a page that gets rebuilt every time you interact with it. When you click a button, change a selection, or enter something, Streamlit reruns your Python code from the top. Normal variables will get reset to their original values.  Session state is like a small memory box for your app. You can store important values there, such as the user's score, number of attempts, or the secret number. The values in session state stay available and survive reruns.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
Commit the code change after each fix.

- What is one thing you would do differently next time you work with AI on a coding task?
Provide more information to AI on what I have and what I expect to get so that AI can give more accurate result without needing to prompt again.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project showed me that AI-generated code can be helpful, but it is not always correct and needs to be reviewed and tested. I learned that I should understand the code and reasoning behind an AI-generated solution instead of simply assuming it will work.