x = input("Zadejte proměnnou x:") # Čeká a uživatele, než zadá číslo. Číslo se následně uloží do proměnné x
y = input("Zadejte proměnnou y:")

x = int(x) # Přetupujeme strna int
y = int(y)

print(f"Proměnná x = {x} a proměnná y = {y}") # Výpis do termunálu - Kontrolujeme co je v x a y.

print("------------------------")
print(f"Příklad {x} + {y}:")
print(f"Sčítání výsledek {x+y}")
print("------------------------")
print(f"Příklad {x} - {y}:")
print(f"Odčítání výsledek {x-y}")
print("------------------------")
print(f"Příklad {x} * {y}:")
print(f"Násobení výsledek {x*y}")
print("------------------------")
print(f"Příklad {x} / {y}:")
print(f"Dělení výsledek {x/y}")
print("------------------------")
print(f"Příklad {x} ^ {y}:") # ^ píšeme levý alt + numerická klávesnice 94
print(f"Mocnění výsledek {x**y}") # Mocníme pomocí **
print("------------------------")
print(f"Příklad {x} √ {y}:")
print(f"Odmocnění výsledek {x**(1/y)}")