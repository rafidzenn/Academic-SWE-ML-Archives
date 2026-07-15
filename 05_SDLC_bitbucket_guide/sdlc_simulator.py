import time

class SDLCProject:
    """An interactive state-machine simulating a software project's lifecycle."""
    
    def __init__(self, project_name):
        self.project_name = project_name
        self.phases = ["Requirements", "Design", "Implementation", "Testing", "Deployment"]
        self.current_phase = 0
        self.quality_score = 100

    def execute_phase(self):
        if self.current_phase >= len(self.phases):
            print(f"\n[SUCCESS] {self.project_name} is live and in Maintenance mode!")
            return False

        phase = self.phases[self.current_phase]
        print(f"\n--- Entering Phase: {phase.upper()} ---")
        
        if phase == "Testing":
            self._simulate_testing()
        else:
            action = input(f"Press [Enter] to complete {phase} or type 'skip' to rush: ").strip().lower()
            if action == 'skip':
                print(f"[WARNING] You rushed {phase}! Technical debt increased.")
                self.quality_score -= 30
            else:
                print(f"[OK] {phase} completed meticulously.")
                time.sleep(1)

        self.current_phase += 1
        return True

    def _simulate_testing(self):
        print("Running automated unit tests...")
        time.sleep(1)
        if self.quality_score < 80:
            print("[ERROR] Critical bugs found due to rushed previous phases!")
            print("[ROLLBACK] Returning to Implementation phase to fix bugs...")
            self.current_phase = 2 # Kick back to implementation
            self.quality_score += 20 # Bug fix recovers some quality
        else:
            print("[PASS] All tests green. Ready for deployment.")

def main():
    print("Welcome to the SDLC Terminal Simulator")
    project = SDLCProject("AI Chatbot V1")
    
    is_active = True
    while is_active:
        is_active = project.execute_phase()

if __name__ == "__main__":
    main()
