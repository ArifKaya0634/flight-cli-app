from datetime import datetime, timedelta

departure_city = input("FlightFinder'a Hoşgeldiniz\nNereden uçacaksınız? ")
arrival_city = input("Nereye uçacaksınız? ")
input_days = int(input("Kaç gün sonra? "))
hours = int(input("Hangi saatte?"))
print(f"{departure_city} → {arrival_city} için uçuşlar:")

def get_prices(input_days): 
 if input_days < 3:
    return [5200, 6800, 4900]
 elif input_days < 10:
    return [3900, 5100, 3600]
 else:
    return [2800, 4200, 2500] 

fiyatlar = get_prices(input_days)

flight_date = datetime.now() + timedelta(days=input_days)
print(f"\n📅 Uçuş tarihi: {flight_date.strftime('%d %B %Y')}")
base_date = datetime.now() + timedelta(days=input_days)
flight_time = base_date + timedelta(hours=hours)
print(f"\n📅 Uçuş: {flight_time.strftime('%d %B %Y %H:%M')}")

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
    return cheapest
cheapest = suggest_cheapest(uçuşlar)

show_flights(uçuşlar)
suggest_cheapest(uçuşlar)

most_expensive = uçuşlar[1]

for flight in uçuşlar:
    if flight[1] > most_expensive[1]:
     most_expensive = flight
print(f"En pahalı uçuş: {most_expensive[0]} - {most_expensive[1]} TL")   

fiyat_farkı = most_expensive[1] - cheapest[1]
print(f"En ucuzla en pahalı arasındaki fiyat {fiyat_farkı} TL")

while True:
 choice = int(input("\nBir uçuş seçin (1-2-3): "))

 if 1 <= choice <= 3:
    break
 else:
    print("Geçersiz seçim! Tekrar dene 😤")

secilen = uçuşlar[choice - 1]
print(f"{secilen[0]} seçildi - {secilen[1]} TL ✈️")
