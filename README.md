# ThothFlow

Simple framework for orchestrating LLM workflows.

It provides simple, abstractions for:
- Agents
- Language models
- State management
- Execution graphs

The goal is to make it easy to experiment with structured reasoning systems,
inspired by frameworks like LangGraph, but with a minimal and flexible design.

## Example

```python
flow = Flow()

flow.add_node("agent", AgentNode(...))
flow.add_edge("start", "agent")

flow.run(input_data)



A "Work" is like a graph, something difficult to do.

While each "Task" is a node in the grap. 

The idea is that a work is resolved by dividing the work 
in tasks

Tasks -> A Node in the graph

Each task receive:
- Something to do: a function/a class with a function run (logic)
- An intelligence, an LLM (here we can pass several ones) (Intelligence)
- A series of tools that can be use to do the task (Tools)

A complex problem (Work) is solved by coordinating smaller intelligent units (Tasks)


🧠 Final mental model (very clean)
Work (Flow) → orchestrates
Task (Node) → executes logic
Agent → provides intelligence
Tools → used by Agent
Scroll (State) → shared data