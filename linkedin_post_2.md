## Agentic Pair Programming in Practice: How I Approached the Build (Part 2) 🧠🤝

In Part 1, I shared how a work problem — dealing with **1000+ emails every week** — became the trigger for my DevDay build.

This post is about **how I approached the solution**, what I learned while building with an agent, and why some decisions mattered more than the code itself.

---

## My Approach

Instead of optimizing for speed or features, I optimized for **learning how to work *with* an agent**, not just alongside one.

That meant being intentional about:
- The context I provided to the model  
- Clear boundaries and explicit rules  
- Tight feedback loops (observe → implement → test)

I stopped thinking of AI as a code generator and started treating it like an **eager intern** — capable, fast, but highly direction-dependent.

---

## Why I Chose MCP Over Standard APIs

I deliberately chose the **Model Context Protocol (MCP)** instead of standard Google APIs — not because it was easier, but because it forced me to think agent-first.

**Did you know?**  
Google’s MCP server is written in **JavaScript**, not Python — which meant my Python backend had to communicate across runtimes.

What MCP gave me:
- A standardized interface for model tools  
- Auth and token lifecycle handled outside my core logic  
- A cleaner mental model for agent-driven workflows  

The trade-off?  
More setup friction — but much deeper learning.

---

## Reality Check: The Hard Parts

This wasn’t a smooth ride.

Getting a Python backend to work with a Node.js-based MCP setup meant dealing with uninstalled dependencies, Node.js setup issues, and plenty of trial-and-error. That friction was uncomfortable — but it exposed where abstractions leak and where agent workflows need extra care in real environments.

---

## A Quick Note on Security

One challenge turned out to be more important than I initially expected:

**Finding ways to provide tokens and secrets without ever exposing them to the AI pair programmer.**

In agentic workflows, the line between “tool access” and “model access” is thin. Designing flows where credentials were usable by the system — but never visible to the agent — required deliberate architectural choices and constant awareness of what the agent could see.

**Did you know?**  
In many agentic setups, you can’t reliably prevent an agent from reading *any* file in its workspace.

That’s why I avoided `.env` files entirely and moved to a **UI-based authentication flow**, storing credentials only in session state. A small design decision — but a meaningful one when experimenting with agents.

---

## The Code

As promised, I’m sharing the **codebase** from this build.

It’s not a polished product — it’s a learning artifact from a one-day buildathon — but it reflects:
- How I structured context  
- How I reasoned about agent boundaries  
- How MCP fits into a real workflow  

👉 **GitHub repo:** *(link here)*

If you explore it, focus less on syntax and more on *why* things are structured the way they are.

---

This build changed how I think about pairing with AI — not as a shortcut, but as a collaborator that performs best with clarity, constraints, and intent.

Curious to hear: **how are you handling security and boundaries in your agentic workflows today?**

---

#AgenticAI #IntelligentEngineering #DevDay #MCP #AIEngineering #Python #BuildInPublic #LearningByBuilding
