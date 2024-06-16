import numpy as np
import matplotlib.pyplot as plt

class ConsciousnessModel:
    def __init__(self, num_entities, interaction_strength, time_steps):
        self.num_entities = num_entities
        self.interaction_strength = interaction_strength
        self.time_steps = time_steps
        self.states = np.random.rand(num_entities)

    def update_states(self):
        for _ in range(self.time_steps):
            interactions = np.random.rand(self.num_entities, self.num_entities) < self.interaction_strength
            self.states += interactions.dot(self.states) / self.num_entities
            self.states = np.clip(self.states, 0, 1)

    def plot_states(self):
        plt.plot(self.states)
        plt.xlabel('Entities')
        plt.ylabel('Consciousness State')
        plt.title('Evolution of Consciousness States')
        plt.show()

# パラメータの設定
num_entities = 100
interaction_strength = 0.01
time_steps = 1000

# モデルの実行
model = ConsciousnessModel(num_entities, interaction_strength, time_steps)
model.update_states()
model.plot_states()

