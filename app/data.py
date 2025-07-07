from datetime import datetime, timedelta
import random

def get_mock_data():
    cities = ["Sydney", "Melbourne", "Brisbane", "Adelaide", "Perth"]
    routes = []
    today = datetime.today()

    for i in range(10):
        origin = random.choice(cities)
        destination = random.choice([c for c in cities if c != origin])
        date = (today + timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d")
        price = random.randint(100, 500)

        routes.append({
            "origin": origin,
            "destination": destination,
            "date": date,
            "price": price
        })

    return routes


def get_real_data():
    cities = ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"]
    routes = [(a, b) for a in cities for b in cities if a != b]
    
    data = []
    today = datetime.today()
    for i in range(10):
        origin, destination = random.choice(routes)
        date = today + timedelta(days=random.randint(1, 30))
        price = random.randint(150, 500)
        data.append({
            "origin": origin,
            "destination": destination,
            "date": date.strftime("%Y-%m-%d"),
            "price": price
        })
    
    return data
