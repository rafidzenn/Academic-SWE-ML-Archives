class Commit:
    def __init__(self, author, message):
        self.author = author
        self.message = message
        self.hash = str(id(self))[-6:] # Simulate a Git SHA hash

    def __str__(self):
        return f"[{self.hash}] {self.message} - by {self.author}"

class Branch:
    def __init__(self, name, base_commits=None):
        self.name = name
        self.commits = base_commits.copy() if base_commits else []

    def add_commit(self, commit):
        self.commits.append(commit)
        print(f"[{self.name}] New commit added: {commit.message}")

class PullRequest:
    """Models a Bitbucket PR lifecycle"""
    def __init__(self, source_branch, target_branch, author):
        self.source = source_branch
        self.target = target_branch
        self.author = author
        self.is_approved = False
        print(f"\n[BITBUCKET] PR Created: Merge '{self.source.name}' into '{self.target.name}' by {self.author}")

    def review(self, reviewer_name, approve=True):
        if approve:
            self.is_approved = True
            print(f"[BITBUCKET] PR Approved by {reviewer_name} ✅")
        else:
            print(f"[BITBUCKET] Changes requested by {reviewer_name} ❌")

    def merge(self):
        if not self.is_approved:
            print("[BITBUCKET ERROR] Cannot merge. PR is not approved!")
            return False
        
        # Simulating the merge of new commits into the target branch
        new_commits = [c for c in self.source.commits if c not in self.target.commits]
        self.target.commits.extend(new_commits)
        print(f"[BITBUCKET SUCCESS] Merged {len(new_commits)} commits into {self.target.name} 🚀")
        return True

def main():
    # 1. Initialize the Bitbucket Repo Main Branch
    main_branch = Branch("main")
    main_branch.add_commit(Commit("Admin", "Initial project setup"))

    # 2. Developer creates a feature branch
    feature_branch = Branch("feature/ai-integration", main_branch.commits)
    
    # 3. Developer does work
    feature_branch.add_commit(Commit("Rafidul", "Added neural network skeleton"))
    feature_branch.add_commit(Commit("Rafidul", "Optimized tensor matrix ops"))

    # 4. Open a Pull Request on Bitbucket
    pr = PullRequest(source_branch=feature_branch, target_branch=main_branch, author="Rafidul")
    
    # 5. Try merging without approval
    pr.merge()
    
    # 6. Team lead reviews, approves, and merges
    pr.review(reviewer_name="SeniorDev", approve=True)
    pr.merge()

if __name__ == "__main__":
    main()
