# Spør brukeren om å velge et alternativ
print("Velg et alternativ:")
print("1. Vis en hilse")
print("2. Vis en morsom melding")
print("3. Avslutt")

# Ta imot input fra brukeren
valg = input("Skriv inn tallet for ditt valg (1, 2 eller 3): ")

# Sjekk hva brukeren har valgt og gi et svar
if valg == "1":
    print("Hei! Hvordan går det?")
elif valg == "2":
    print("Hvorfor kan ikke syklere holde hemmeligheter? Fordi de sladrer så fort!")
elif valg == "3":
    print("Programmet avsluttes. Ha en fin dag!")
else:
    print("Ugyldig valg. Vennligst prøv igjen.")