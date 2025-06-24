import numpy as np
import matplotlib.pyplot as plt

def probability_density(x, L):
    """Calcula a densidade de probabilidade para um elétron confinado em uma caixa."""
    psi = np.sqrt(2/L) * np.sin(np.pi * x / L)
    probability = np.abs(psi)**2
    return probability

def plot_probability_density(L):
    """Plota o gráfico da densidade de probabilidade para um elétron confinado em uma caixa."""
    x = np.linspace(0, L, 1000)
    y = probability_density(x, L)

    plt.plot(x, y)
    plt.xlabel('Posição')
    plt.ylabel('Densidade de Probabilidade')
    plt.title('Elétron Confinado em uma Caixa de Tamanho L')
    plt.grid(True)
    plt.show()

# Tamanho da caixa
L = 1.0

# Chama a função para plotar o gráfico da densidade de probabilidade
plot_probability_density(L)

