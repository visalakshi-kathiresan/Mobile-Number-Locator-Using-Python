import phonenumbers
from phonenumbers import geocoder, carrier


def locate_indian_number(number):
    try:
        parsed_number = phonenumbers.parse(number, "IN")

        if not phonenumbers.is_valid_number(parsed_number):
            return "Invalid number", "N/A", "N/A"

        location = geocoder.description_for_number(parsed_number, "en")

        service_provider = carrier.name_for_number(parsed_number, "en")

        return location, service_provider, "Valid"
    except phonenumbers.NumberParseException as e:
        return f"Error: {e}", "N/A", "N/A"

def validate_indian_number(number):
    if not number.startswith("+91"):
        return False
    if len(number) != 13:
        return False
    return True

if __name__ == "__main__":
    print("Indian Mobile Number Locator")
    print("----------------------------")

    number = input("Enter the mobile number (e.g., +919876543210): ").strip()

    if not validate_indian_number(number):
        print("Error: Please enter a valid Indian mobile number with the +91 prefix.")
    else:
        location, carrier_info, status = locate_indian_number(number)
        print("\nResults:")
        print(f"Number: {number}")
        print(f"Location: {location}")
        print(f"Carrier: {carrier_info}")
        print(f"Status: {status}")
