# Día 0 · Tipos básicos y casting

# Bases numéricas
print(0b101)        # binario      -> 5
print(0o12)         # octal        -> 10
print(0xA + 1)      # hexadecimal  -> 11

# type()
print(type(1e3))    # <class 'float'>
print(type(7 / 2))  # <class 'float'>: / siempre da float

# bool es un int
print(True + True * 3)   # 4

# Casting
print(int(7.99))         # 7: corta, no redondea
print(bool("False"))     # True: texto no vacío
print(int("3") + int(2.5))  # 5