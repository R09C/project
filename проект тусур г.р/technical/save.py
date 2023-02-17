def save(mass,name):
    with open(name,'w') as f:
        for item in mass:
            f.write(f"{str(item)}\n")