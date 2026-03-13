# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  
  It looks like a simple game with basic functions. The game looks unfinished and has many bugs and logic errors. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  New game button creates the game but does not reset attempts nor clear the queue.

  Score goes to negative when incorrectly answered.

  The range is not correctly defined for difficulty
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  Claude Code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  The range for diffculty was correctly identified. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  N/A

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  I cross checked the code and also play tested it. I asked copilot to write some test cases which also passed.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  At first some tests where failing so I took a look and figured the tests was not in sync of the funstions, So with the help of copilot I figured out the problem and fixed it.

- Did AI help you design or understand any tests? How?

  I gave instructions to copilot to test the function in some ways I think and also to add some suggested tests to make sure there are no errors.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.



- What is one thing you would do differently next time you work with AI on a coding task?



- In one or two sentences, describe how this project changed the way you think about AI generated code.

