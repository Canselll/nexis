query = f"""
    SELECT flight.id, flight.flight, flight.source_city, flight.destination_city, flight.price , flight.departure_date ,flight.arrival_date, classes.class, airline.airline
    FROM flight
    INNER JOIN classes ON flight.id = classes.id
    INNER JOIN airline ON flight.id = airline.id
    WHERE flight.departure_date >= %s AND flight.departure_date <= %s;
"""