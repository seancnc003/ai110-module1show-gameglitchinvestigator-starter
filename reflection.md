# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  Answer:
  1. The hint system was wrong. It outputs lower when it should be higher and higher when it should be lower.
  For example, the secret is 78 and when I put in 5 the hint is lower and when I put in 80, the hint is higher.

  This should be reversed as to give correct hints.

  2. The default difficulty settings do not make sense and they should be changed. 
  Easy's range is 1 to 20 with 6 attempts allowed, Medium's range is 1 to 100 with 8 attempts allowed, and
  Hard's range is 1 to 50 with 5 attempts allowed.

  A more accurate difficulty settings would make it be:
    * Easy:   range 1 to 20, 8 attempts
    * Medium: range 1 to 50, 6 attemps
    * Hard:   range 1 to 100, 5 attempts

  3. Game does not reset after a win or a loss only when game is reset during the middle of a game. 
  Only the secret changes and you can't put in a new number and you don't have attempts.

  This should be changed as to allow users to actually play a new game.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Answer: 
The AI tools that I used was Claude Code Opus and Sonnet 4.6 Medium difficulty and Cursor Composer 1.5.

The code taht the AI suggested to fix the two bugs I picked, fixing the hints and starting a new game
was correct. I verified the result by manually going through the game and checking that it does
what it said it does.

One example of an AI suggestion that was incorrect was the tests that it generated. I had told it
to generate tests for the bug fixes that we did. The first test was correct about the hint being 
correct now. The second test it gave me was checking the difficulty settings and if it was logical,
this was a bug that I identified but did not choose to correct. I had to mention to the AI explicitly
to write a test for the other bug which was about whether or not a new game starts after a win or a loss. I verified the result by looking at the tests file.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

Answer:  
I decided whether a bus was really fixed or not through the eye test and manually running
the game. When the hints was now correct and I could really play a new game, that's when
I decided the bugs were fixed.

Two tests I ran was checking if the hints were correct. When an example game showed that
when the secret is 55, I put in 5 and it gave me higher hint and when I put in 65 and it showed
me lower, that's when I knew it was correct.
For the other test. When I get the answer right, right away and I click new game and I am able
to enter new numbers, that how I knew that was correct.
It showed me that my code was now correct and was doing what I expected it too.

Yes, AI did help me design my tests. I had never ran pytest before so AI was instrumental
in me being able to create the tests and run it.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit is reloaded from the full page with the code top to bottom all the time through the reruns 
everytime the user interacts with the app with hitting a button for example. 
Session state is important for the persistence and keeping of the memory. The session states allow 
for data to be stored especially in this game with the secret number, number of attempts, game status,
and history.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One strategy from this project that I want to reuse in future labs is being able to know 
at least roughly which parts of the code deals with what's on the program. Being able to know
quickly where the hints section or where new game is in the codebase made debugging with AI faster
and also helped me understand the changes that I am putting in better.

One thing I would do differently is be more critical of the code. I didn't have previous experience with
pytest, so I could've dug deeper into the code changes that the AI was implementing.

This project changed the way I thought about AI generated code because it showed me how important context
and double checking AI generated code is. I had mentioned it previously, but when I had told the AI
to write test cases for me, it didn't write the test cases I wanted it to do. It didn't understand
my intent right away and it was on me to be clearer. It was a good catch that I caught it early and not 
later on.
