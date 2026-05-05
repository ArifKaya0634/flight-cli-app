from datetime import datetime, timedelta

departure_city = input("FlightFinder'a Hoşgeldiniz\nNereden uçacaksınız? ")
arrival_city = input("Nereye uçacaksınız? ")
days = int(input("Kaç gün sonra? "))

print(f"{departure_city} → {arrival_city} için uçuşlar:")

def get_prices(days): 
 if days < 3:
    return [5200, 6800, 4900]
 elif days < 10:
    return [3900, 5100, 3600]
 else:
    return [2800, 4200, 2500] 

fiyatlar = get_prices(days)

def create_flights(fiyatlar):
 return [
    ["Pegasus", fiyatlar[0]],
    ["THY", fiyatlar[1]],
    ["AJet", fiyatlar[2]]
]

uçuşlar = create_flights(fiyatlar)

def show_flights(uçuşlar):
    for index, flight in enumerate(uçuşlar, start=1):
        print(f"{index}. {flight[0]} - {flight[1]} TL")

def suggest_cheapest(uçuşlar):
    cheapest = uçuşlar[0]

    for flight in uçuşlar:
        if flight[1] < cheapest[1]:
            cheapest = flight

    print(f"\nEn ucuz uçuş: {cheapest[0]} - {cheapest[1]} TL")

show_flights(uçuşlar)
suggest_cheapest(uçuşlar)

while True:
 choice = int(input("\nBir uçuş seçin (1-2-3): "))

 if 1 <= choice <= 3:
    break
 else:
    print("Geçersiz seçim! Tekrar dene 😤")

secilen = uçuşlar[choice - 1]
print(f"{secilen[0]} seçildi - {secilen[1]} TL ✈️")
