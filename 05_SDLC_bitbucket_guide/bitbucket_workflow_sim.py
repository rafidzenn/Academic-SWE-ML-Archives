import hashlib
import time

class TemporalSnapshot:
    """Represents a 'Commit' - A frozen state of the universe at a specific time."""
    def __init__(self, author, event_modification):
        self.author = author
        self.modification = event_modification
        self.timestamp = time.time()
        # Create a unique SHA-256 hash, exactly how Git generates commit hashes
        hash_string = f"{author}{event_modification}{self.timestamp}".encode('utf-8')
        self.temporal_hash = hashlib.sha256(hash_string).hexdigest()[:8]

    def __str__(self):
        return f"[Snapshot {self.temporal_hash}] {self.author} altered reality: '{self.modification}'"

class Timeline:
    """Represents a 'Branch' - A sequence of temporal snapshots."""
    def __init__(self, name, origin_timeline=None):
        self.name = name
        # If branching from another timeline, inherit its history
        self.history = origin_timeline.history.copy() if origin_timeline else []
        self.reality_state = origin_timeline.reality_state.copy() if origin_timeline else {}
        if origin_timeline:
            print(f"🌌 [TIMELINE SPLIT] Divergent timeline '{self.name}' created from '{origin_timeline.name}'.")

    def alter_event(self, author, file_name, new_content):
        """Simulates making a commit and changing a file."""
        snapshot = TemporalSnapshot(author, f"Modified {file_name}")
        self.history.append(snapshot)
        self.reality_state[file_name] = new_content
        print(snapshot)

class BitbucketTemporalCouncil:
    """Represents Bitbucket's Pull Request and Merge Conflict resolution system."""
    @staticmethod
    def open_pull_request(source: Timeline, target: Timeline, author: str):
        print(f"\n⚖️ [BITBUCKET PR CREATED] {author} requests to merge '{source.name}' into '{target.name}'.")
        print("🔍 Initiating Temporal Paradox Scan (Merge Conflict Check)...")
        time.sleep(1)

        paradox_detected = False
        for file, content in source.reality_state.items():
            # Check if the target timeline altered the same event independently
            if file in target.reality_state and target.reality_state[file] != content:
                print(f"🚨 [PARADOX DETECTED - MERGE CONFLICT] The event '{file}' was altered differently in both timelines!")
                paradox_detected = True

        if paradox_detected:
            print("❌ [PR REJECTED] You must resolve the paradox (merge conflicts) locally before the Council allows this merge.\n")
            return False
        
        print("✅ [PR APPROVED] No paradoxes detected. The timelines can safely converge.")
        return True

    @staticmethod
    def converge_timelines(source: Timeline, target: Timeline):
        """Simulates a Git Merge."""
        target.history.extend(source.history)
        target.reality_state.update(source.reality_state)
        print(f"🌀 [TIMELINES CONVERGED] '{source.name}' successfully merged into '{target.name}'. Reality is stable.\n")

def run_simulation():
    print("=== INITIALIZING VERSION CONTROL MULTIVERSE SIMULATOR ===\n")

    # 1. Initialize the Main Branch
    alpha_timeline = Timeline("Main-Branch (Alpha)")
    alpha_timeline.alter_event("System", "database.py", "version_1")

    # 2. Developer 1 creates a feature branch
    dev_timeline = Timeline("Feature-AI-Model", origin_timeline=alpha_timeline)
    dev_timeline.alter_event("Rafidul", "neural_net.py", "added_pytorch_model")

    # 3. Simulate a concurrent change on the Main branch (Someone else merged while you were working)
    print("\nMeanwhile, in the Alpha Timeline...")
    alpha_timeline.alter_event("Senior_Dev", "database.py", "version_2_optimized")

    # 4. Rafidul attempts to open a PR on Bitbucket
    council = BitbucketTemporalCouncil()
    pr_safe = council.open_pull_request(source=dev_timeline, target=alpha_timeline, author="Rafidul")

    if pr_safe:
        council.converge_timelines(dev_timeline, alpha_timeline)

    # 5. Let's force a Merge Conflict (Paradox) to show how the system handles it
    print("--- DEMONSTRATING A MERGE CONFLICT ---")
    rogue_timeline = Timeline("Hotfix-Database", origin_timeline=alpha_timeline)
    # Both timelines will now try to change the exact same file in different ways
    rogue_timeline.alter_event("Intern", "database.py", "version_3_broken")
    alpha_timeline.alter_event("Senior_Dev", "database.py", "version_3_secure")
    
    council.open_pull_request(source=rogue_timeline, target=alpha_timeline, author="Intern")

if __name__ == "__main__":
    run_simulation()
