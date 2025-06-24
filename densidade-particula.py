

import numpy as np
import matplotlib.pyplot as plt

def probability_density(x, L):
    """Calcula a densidade de probabilidade para uma partícula clássica confinada em uma caixa."""
    probability = np.where(np.logical_and(x >= 0, x <= L), 1/L, 0)
    return probability

def plot_probability_density(L):
    """Plota o gráfico da densidade de probabilidade para uma partícula clássica confinada em uma caixa."""
    x = np.linspace(0, L, 1000)
    y = probability_density(x, L)

    plt.plot(x, y)
    plt.xlabel('Posição')
    plt.ylabel('Probabilidade')
    plt.title('Partícula Clássica Confinada em uma Caixa de Tamanho L')
    plt.grid(True)
    plt.show()

# Tamanho da caixa
L = 1.0

# Chama a função para plotar o gráfico da densidade de probabilidade
plot_probability_density(L)