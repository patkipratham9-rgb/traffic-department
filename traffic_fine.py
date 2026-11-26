FINES = {
    "No Helmet": 500,
    "Signal Jumping": 1000,
    "Over Speeding": 2000,
}


def calculate_fine(violation_type):
    return FINES[violation_type]


if __name__ == "__main__":
    print("--- Traffic Violation Fine Rates ---")
    print("No Helmet: Rs. 500 | Signal Jumping: Rs. 1000 | Over Speeding: Rs. 2000")

    vehicle_no = input("\nVehicle registration number: ")
    violation = input("Type of violation (No Helmet / Signal Jumping / Over Speeding): ")

    fine = calculate_fine(violation)

    print("\n--- Fine Receipt ---")
    print("Vehicle Registration Number:", vehicle_no)
    print("Violation Type:", violation)
    print("Total Fine Amount: Rs.", fine)