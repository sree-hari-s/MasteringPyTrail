# Forking and Pull Requests

## Forking

- Forking is creating a personal copy of someone else's project.
- Click "Fork" on GitHub to create your copy.

## Pull Requests

- **Open a Pull Request (PR):**
  - When contributing changes to a repository.
- **Merge a Pull Request:**
  - After reviewing changes, merge them into the main branch.

## Example Workflow

1. Fork the repository on GitHub.
2. Clone your forked repository locally.

   ```bash
   git clone <your_fork_url>
   cd <repository_folder>
   ```

3. Create a new branch for your changes.

   ```bash
   git checkout -b feature/new-feature
   ```

4. Make and commit changes.

   ```bash
   git add .
   git commit -m "Implement new feature"
   ```

5. Push changes to your fork.

   ```bash
   git push origin feature/new-feature
   ```

6. Open a Pull Request on GitHub.
7. Collaborate and address feedback.
8. Merge the Pull Request.
