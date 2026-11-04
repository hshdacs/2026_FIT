import numpy as np
import matplotlib.pyplot as plt

y = np.array( [1, 2, 3.7, 4] )
plt.plot(y)

plt.plot( np.array([1,2,3,4]), np.array([2, 3, 4, 4.5]), label="Some data" )
plt.plot( np.array([2, 3.5, 4.2, 5]), label="Other data" )

plt.title("Ein hübscher Plot")
plt.legend()
plt.savefig("my_plot.jpg", dpi=300)
plt.show()

x = np.linspace(0, 2*np.pi) # Generiere Werte von 0 bis 2pi Schrittweite 1
y = np.sin(x*4) * x
plt.plot(x, y)
plt.plot(x, np.sin(x))
plt.ylabel("f(x)")
plt.xlabel("x")
plt.title("f(x) = x*sin(4x)")
plt.savefig("funktion.pdf")
plt.show()

x1 = np.linspace(-1, 1, 10)
x2 = np.linspace(-1, 1, 1000)
def f1(x):
    return np.sin(1/x)

plt.plot(x2, f1(x2), label="{:d} Punkte".format(len(x2)))
plt.plot(x1, f1(x1), label="{:d} Punkte".format(len(x1)))
plt.legend()
plt.ylabel("f(x)")
plt.xlabel("x")
plt.title("Vergleich der Dichte von Punkten")
plt.show()

x = np.linspace(0, 5, 12) # [0,5] Werte 0 bis 5, Schritweite 0.5
plt.plot(x, 1/(x+1), "--m") # --- Linie in magenta
plt.plot(x, 1/(x+2), "Dc")  # Routen in Cyan
plt.plot(x, 1/(x+3), "-.b") # -.- Linie in Blau
plt.xlabel("x")
plt.show()
