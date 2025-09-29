import math

def calculate_bill (consump: int, customer_type: str, age:int):
    if consump < 0 or consump > 1000000:
        raise ValueError("So kWh khong hop le")
    if consump <= 50:
        cost = consump * 0.60
    elif consump <= 100:
        cost = 50 * 0.60 + (consump - 50) * 0.80
    elif consump <= 200:
        cost = 50 * 0.60 + 50 * 0.80 + (consump - 100) * 1.00
    else:
        cost =  50 * 0.60 + 50 * 0.80 + 100 * 1.00 + (consump - 200) * 1.20
    
    # Phu phi cho business
    if customer_type.lower() == "business":
        cost *= 1.10
    
    #Giam gia cho nguoi lon tuoi va tre nho
    if age >= 65 or age <= 14:
        cost *= 0.90
    
    return round(cost, 2)