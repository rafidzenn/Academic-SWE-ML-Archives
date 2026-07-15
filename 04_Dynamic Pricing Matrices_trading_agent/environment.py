import numpy as np

class MarketEnvironment:
    """Simulates a volatile asset marketplace index."""
    def __init__(self, history_length=100):
        np.random.seed(10)
        self.prices = np.sin(np.linspace(0, 20, history_length)) * 10 + 50 + np.random.normal(0, 1, history_length)
        self.current_step = 0
        self.max_steps = history_length - 1

    def reset(self):
        self.current_step = 0
        return self.get_state()

    def get_state(self):
        # State: Return current step asset price point
        return np.array([self.prices[self.current_step]])

    def step(self, action):
        # Actions: 0 = Hold, 1 = Buy, 2 = Sell
        current_price = self.prices[self.current_step]
        self.current_step += 1
        next_price = self.prices[self.current_step]
        
        reward = 0
        if action == 1:   # Buy
            reward = next_price - current_price
        elif action == 2: # Sell
            reward = current_price - next_price
            
        done = self.current_step >= self.max_steps
        return self.get_state(), reward, done
