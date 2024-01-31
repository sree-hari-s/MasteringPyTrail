# GitHub

GitHub is a web-based platform that hosts Git repositories and provides collaborative features like pull requests, code review, and issue tracking.

## Basic Operations

### Basic Commands

- **Initialize a Git Repository:**

  ```bash
  git init
  ```

- **Add Changes:**

  ```bash
  git add <file>
  ```

- **Commit Changes:**

  ```bash
  git commit -m "Commit message"
  ```

- **Check Status:**

  ```bash
  git status
  ```
  
### GitHub and Remote Repositories

- **Clone Repository:**

  ```bash
  git clone <repository_url>
  ```

- **Push Changes to Remote:**

  ```bash
  git push origin <branch_name>
  ```

- **Pull Changes from Remote:**

  ```bash
  git pull origin <branch_name>
  ```

### .gitignore

- Create a `.gitignore` file to specify files or directories to be ignored by Git.

  Example `.gitignore`:

  ```plaintext
  # Ignore log files
  *.log

  # Ignore directories
  node_modules/
  ```

### Branching and Merging

- **Create a New Branch:**

  ```bash
  git branch <branch_name>
  git checkout -b <branch_name>  # Create and switch to a new branch
  ```

- **Merge Branches:**

  ```bash
  git merge <branch_name>
  ```
