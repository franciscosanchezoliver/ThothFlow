# ThothFlow: Orchestrating Git Repos as Tasks

Each git repo is a task and each repo defines:
- Input Contract
- Output Contract

A Work is a graph of repos, connected via inputs/output. The work defines a 
flow (orchestration layer between repos).

Each repo become a reusable black box (like microservices).

Once a repo (task) is written, it can be orchestrated in multiple flows

## Advantages:

### Reusability

As each repo does a task, it can be orchestrated in multiple flows. 
Makes projects composable in a structured way.


### Language Agnostic

The idea is to be able to make projects composable, language agnostic (you don't 
care what language was used to resolve the problem). 

### Decentralized Orchestration

Repositories can be on GitHub, GitLab, a private Git server, or a combination.
