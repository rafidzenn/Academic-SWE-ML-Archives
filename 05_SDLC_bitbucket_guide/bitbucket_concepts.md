## Bitbucket & Enterprise Version Control

Bitbucket is a Git-based source code repository hosting service. While similar to GitHub, it integrates heavily with enterprise tools (like Jira) and emphasizes CI/CD pipelines and private organizational codebases.

### Core Concepts Intuitive Breakdown:
* **Repository (Repo):** The master folder where all project files and historical changes live.
* **Master/Main Branch:** The "Holy Grail" of the code. This is what is currently live in production. You never code directly here.
* **Feature Branch:** A parallel universe. You clone the main code into a safe sandbox, build your new feature, and test it without breaking the live app.
* **Commit:** Saving your progress in the timeline with a descriptive message ("Fixed login bug").
* **Pull Request (PR):** A formal request asking the team to review your Feature Branch and merge (combine) it back into the Main Branch.
* **Merge Conflict:** When two developers edit the exact same line of code in different branches, and Bitbucket asks a human to decide which version wins.
