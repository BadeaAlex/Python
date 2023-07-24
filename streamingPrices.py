def compare_prices(service_prices):
    sorted_services = sorted(service_prices.items(), key=lambda x: x[1])
    
    print("Streaming Service Prices Comparison:")
    print("-----------------------------------")
    
    for service, price in sorted_services:
        print(f"{service}: ${price:.2f}")

def get_service_prices():
    service_prices = {}
    
    num_services = int(input("Enter the number of streaming services: "))
    
    for i in range(num_services):
        service = input(f"Enter the name of streaming service {i+1}: ")
        price = float(input(f"Enter the price for {service}: $"))
        service_prices[service] = price
    
    return service_prices

# Example usage
print("Streaming Service Price Comparison")
print("----------------------------------")

services = get_service_prices()
print("\nComparing prices...")
compare_prices(services)
