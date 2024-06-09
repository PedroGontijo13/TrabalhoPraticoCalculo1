import re

def parse_polynomial(polynomial):
    # Removing spaces and split the polynomial string
    polynomial = polynomial.replace(" ", "")
    terms = re.findall(r'([+-]?\d*\.?\d*)x\^?(\d*)', polynomial)
    
    degree = max(int(exp) if exp else 1 for _, exp in terms)
    coefficients = [0] * (degree + 1)
    
    for coeff, exp in terms:
        coeff = float(coeff) if coeff else 1.0
        exp = int(exp) if exp else 1
        coefficients[exp] += coeff

    if polynomial[-1] not in 'x0123456789':
        coefficients[0] += float(polynomial[-1])
    
    return coefficients[::-1]

def derivative(coefficients):
    derived_coeffs = []
    for i in range(1, len(coefficients)):
        derived_coeffs.append(coefficients[i] * i)
    return derived_coeffs

def evaluate_polynomial(coefficients, x):
    result = 0
    for i, coeff in enumerate(coefficients):
        result += coeff * (x ** i)
    return result

def polynomial_to_string(coefficients):
    terms = []
    for i, coeff in enumerate(coefficients):
        if coeff != 0:
            if i == 0:
                terms.append(f"{coeff}")
            elif i == 1:
                terms.append(f"{coeff}x")
            else:
                terms.append(f"{coeff}x^{i}")
    return " + ".join(terms[::-1])

def tangent_line(f_prime, f_at_a, a):
    slope = f_prime
    intercept = f_at_a - slope * a
    return f"y = {slope}x + {intercept}"

def main():
    polynomial = input("Qual função f(x) deseja calcular a derivada? ")
    coefficients = parse_polynomial(polynomial)
    
    print(f"f(x) = {polynomial_to_string(coefficients)}")
    
    derived_coeffs = derivative(coefficients)
    print(f"f'(x) = {polynomial_to_string(derived_coeffs)}")
    
    if input("Deseja calcular o valor funcional f'(a)? (s/n) ").lower() == 's':
        a = float(input("Qual o valor de a? "))
        f_at_a = evaluate_polynomial(coefficients, a)
        f_prime_at_a = evaluate_polynomial(derived_coeffs, a)
        print(f"a = {a}, f(a) = {f_at_a}, f'(a) = {f_prime_at_a}, P = ({a}, {f_at_a})")
        
        if input("Deseja calcular a equação da reta tangente ao gráfico de f(x) no ponto P? (s/n) ").lower() == 's':
            tangent_eq = tangent_line(f_prime_at_a, f_at_a, a)
            print(f"A equação da reta tangente ao gráfico de f(x) no ponto P = ({a}, {f_at_a}) será: {tangent_eq}")

if __name__ == "__main__":
    main()
