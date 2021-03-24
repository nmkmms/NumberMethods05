import numpy as np
from numpy.polynomial.polynomial import Polynomial as Poly
import matplotlib.pyplot as plt


x_values = np.arange(-1, 1.25, 0.25)
y_values = [
    -1.1071487177940905030,
    -0.98279372324732906799,
    -0.78539816339744830962,
    -0.46364760900080611621,
    0,
    0.46364760900080611621,
    0.78539816339744830962,
    0.98279372324732906799,
    1.1071487177940905030
]


def plot(polynomial):
    x_step = np.arange(-2, 2, 0.01)
    plt.figure(figsize=(16, 9))
    plt.plot(x_step, polynomial(x_step), 'b')

    plt.title('Lagrange Basis Polynomials')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()


def lagrange(no):
    total = Poly([1])
    current_x = x_values[no]
    for i in range(len(x_values)):
        if i == no:
            continue
        temp_poly = Poly([-x_values[i], 1]) / (current_x - x_values[i])
        total = total * temp_poly
        # print(temp_poly)

    return total


def main():
    lagrange_basises = [lagrange(i) for i in range(len(x_values))]
    lagrange_coefs = sum([poly * coef for poly, coef in zip(lagrange_basises, y_values)])

    print(f'Builded polynomial:\n{lagrange_coefs}')

    plot(lagrange_coefs)
    assertion(lagrange_coefs)


def assertion(lagrange_poly):
    print('=' * 50)
    print('COMPARING:')
    for value in np.arange(-0.9, 1.2, 0.6):
        value = round(value, 3)
        real = np.arctan(2 * value)
        mine = lagrange_poly(value)
        print(f'L({value}) = {mine:.9f}\tf({value}) = {real:.9f}')


if __name__ == '__main__':
    main()
