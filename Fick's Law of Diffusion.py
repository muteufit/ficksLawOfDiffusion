from sympy import symbols, diff

def fick_law(diffusion_coefficient, concentration, position):
    # Define symbolic variables
    D, C, x = symbols('D C x')

    # Define Fick's Law equation
    fick_equation = -D * diff(C, x)

    # Substitute values into the equation
    result = fick_equation.subs({D: diffusion_coefficient, C: concentration, x: position})
    
    return result

print(    """
    Calculate the diffusion flux using Fick's Law.

    Parameters:
    - diffusion_coefficient: Diffusion coefficient of the substance.
    - concentration: Concentration of the diffusing substance.
    - position: Position coordinate.

    Returns:
    The diffusion flux.
    """
)
diffusion_coefficient = float(input('Enter diffusion coefficient: '))
concentration = float(input('Enter the concentration: ')) 
position = float(input('Enter position: ')) 

result = fick_law(diffusion_coefficient, concentration, position)
print(f"The diffusion flux is {result}.")
