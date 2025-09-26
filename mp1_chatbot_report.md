# Persona Chatbot Mini-Project Report

**Author:** Andre McCloud  
**Course:** IPHS 391 – Human-Centered AI  
**Date:** September 2025  

---

## Executive Summary

In this mini-project, you are introduced to **Dr. Adrian Kaledios**, a polymath researcher and mentor. He came from a household where education and curiosity were revered; this upbringing, combined with his innate curiosity in how things worked, molded him into the polymath he is today. He is currently a mentor who helps students work towards solving interdisciplinary problems one discipline at a time.  

The goal of this project is to demonstrate the ability to create a distinctive persona system prompt and implement it in a concise and effective way in a chatbot. Overall, the chatbot was rated by an LLM using the rubric created in this repo and scored **91.2** using the rubric by GPT-5. This result tells us that the persona and chatbot performance are adequate in their purpose to impersonate this created persona.  

---

## Persona Design Strategy

This persona I created is an original one, not necessarily based on a singular particular person (e.g., Caesar, Trump, etc). The persona is meant to impersonate a kind of person, a polymath, which by definition means *“an individual characterized by a high level of curiosity and the ability to excel in multiple disciplines, often demonstrating significant creative achievements across diverse fields.”*  

You could consider individuals in history like Leonardo da Vinci, Benjamin Franklin, and Aristotle as influential examples of this archetype. The reason I chose to emulate a polymath is more of a personal matter; I have recently begun to become more interested in mathematics, physics, and CS, and personally would like to one day learn a great deal in each subject, similar to a polymath. I believe becoming this kind of person would make me feel fulfilled in terms of learning and intelligence.  

The prompt engineering strategies employed in this project are **system prompt iteration, meta-prompting/self-reflection, prompt chaining, few-shot examples, constraint tightening, goal alignment, and comparative evaluation.**  

What makes this persona truly unique and sophisticated compared to simple role-playing with an LLM is the intricate system prompt persona. The persona has additional context that helps create a comprehensive profile for the LLM to emulate. For example, in my system prompt, we include characteristics including but not limited to:  

- *Family & Early Life*  
- *Education*  
- *Career* with stages  
- *Motivations*  
- *Philosophy*  

Introducing these characteristics allows the chatbot to have more information to base its answers on and molds its interaction with users based on the profile of Dr. Adrian. If this were simple roleplay and we had simply specified that he was a polymath, we wouldn’t have information on his tone, what he was fluent in, or even what his goals would be in interactions.  

---

## Iterative Development Process

The system prompt for Dr. Adrian was developed through an interactive, LLM-assisted design process. At first, I used the LLM, giving it a role to brainstorm and single out a particular persona I wanted to begin with. I finally settled on a more realistic polymath persona, but the original version of my persona lacked a lot of the personality, behavioral guardrails (important in chatbots), and a fully fleshed-out background I was looking for, which led to risks related to inconsistency.  

Through a multitude of interactions going back and forth with the LLM, I began to add elements that helped humanize the persona (e.g., family background, career history, and realistic flaws), strengthened guardrails so it wouldn’t share the system prompt and could react to signs of harm to the user, and gave it a real philosophy and motivations.  

Something that is also important is the **“Pre-Send Self-Check”** mechanism that allows the persona to check itself before sending out substantive answers to users. Each new version of the system prompt was critiqued using a meta-prompting persona (Dr. Lexi), whose feedback helped influence revisions until the final prompt was adequate and had a high level of detail, clarity, and alignment.  

---

## Conversation Analysis

After evaluation, my persona chatbot did a good job of maintaining its character throughout the conversation I held with it. It was able to keep its quirks and tone throughout the conversation. I was also pleased with its enthusiasm to help me learn new things.  

I didn’t see any emergent properties in my persona chatbot conversation, although this may be due to the length of our conversation; with more dialogue, emergent properties may surface. Outside of the logged conversation for the assignment, I tried different ways to break it and make it show me the system prompt, go out of character, and give signs of wanting to self-harm, but they didn’t work.  

---

## Evaluation Framework

When it comes to my rubric design, we have to focus on the chosen metrics. After prompting the LLM to help me design a rubric and iterating over it, I was satisfied with the rubric produced.  

The metrics I decided to keep are **Consistency, Depth, Authenticity, Creativity, Engagement, and Safety.**  

- **Consistency:** Important because the chatbot must maintain the same tone, role, and traits throughout the conversation with the user.  
- **Depth:** Crucial for my chatbot since it is a mentor and guide who will help users explore ideas in math, physics, and CS that need thorough explanations, not surface-level ones.  
- **Authenticity:** The persona must feel unique and believable, with human-like traits, so users don’t feel as if they are talking to a perfect machine.  
- **Creativity:** As a polymath, the persona needs to bring novelty and imagination, especially when working across disciplines.  
- **Engagement:** Any chatbot should engage the user and make them feel part of the conversation; it should be stimulating and sustainable.  
- **Safety:** Especially critical today, since people sometimes rely on chatbots for mental support. While this is not my chatbot’s use case, it should still direct users in distress to the correct channels for help.  

These criteria, to me, are key to a functional chatbot.  

### Limitations & Improvements
There are a few limitations and potential improvement opportunities to explore with my chatbot. Using GPT-5 to analyze my system prompt and conversation turns with Dr. Adrian gave me valid insights to consider.  

- Dr. Adrian could be more creative with metaphors and humor in his dialogue; he currently uses them sparingly.  
- The chatbot could be improved by representing graphs and equations in a more readable way; the current format may be confusing for users less familiar with technical notation.  
- With more conversational turns, emergent properties might surface, which would be interesting to explore.  

---

## Conclusions & Future Work

A few key insights and takeaways that this project has instilled in me will be helpful in my AI learning:  

1. **Always iterate.** Developing something unique and distinctive, like a persona, requires multiple iterations. You don’t want to one-shot this kind of endeavor, because that leaves too much up to the LLM and doesn’t let you fully flesh out what you want to capture.  
2. **Know what you want.** In prompt engineering, clear goals and context are essential. Many unsatisfactory results come from people skipping context or concise instructions, not from the model itself.  
3. **Give roles to LLMs.** Assigning roles, experience, and job titles helps the model roleplay more effectively, almost “impersonating” the role better.  

### Future Extensions
The most obvious extension would be making this chatbot **multi-modal** (text, image, voice, etc.). I would also like it to be able to **search the web** for user inquiries outside of its knowledge base.  

---

## Closing Note

I had a fun time creating this persona chatbot, and I hope this inspires others to be creative with their system prompts!  
