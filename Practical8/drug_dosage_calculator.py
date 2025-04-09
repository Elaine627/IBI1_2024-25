def drug_dosage_calculator(weight, strength):
    """
    Input: individual's weight (in kg);strength of paracetamol(either 120mg/5ml or 250mg/5ml)
    Returns the volume of paracetamol required
    """
    errors = [] # Collects error messages
    
    # Check whether reasonable input had been provided
    if weight < 10 or weight > 100:
        errors.append("Error: the supplied weight is outwith the expected range. Please double check your input.")   
    if strength.replace(" ","") != '120mg/5ml' and strength.replace(" ","") != '250mg/5ml': # To prevent error caused by unexpected spaces in the input
        errors.append("Error: the paracetamol strength does not match an expected concentration. Please double check your input.")
    if errors:
        for error in errors:
            print(error)
        return('Error:Please double check your input.')
    # Calculate volume of paracetamol required
    else:
        dose = weight*15
        if strength.replace(" ","") == '120mg/5ml':
            volume = dose/24
        if strength.replace(" ","") == '250mg/5ml':
            volume = dose/50
        return volume

# Example function call
example = drug_dosage_calculator(45,'120mg/5ml')
print(f"Here's an example function call, with weight of 45kg and paracemol strength of 120mg/5ml:The volume of paracetamol required (in ml) is: {example}")
weight = float(input("Please tell us your weight(in kg):"))
strength = str(input("What will be the strength of paracetamol?"))
output = drug_dosage_calculator(weight, strength) # Call the function
print(f"The volume of paracetamol required (in ml) is: {output}")