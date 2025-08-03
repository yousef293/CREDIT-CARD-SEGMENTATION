import json

def convert_string_numbers_to_numbers():
    # Read the original data
    with open('data.json', 'r') as file:
        data = json.load(file)
    
    # Convert string numbers to actual numbers for all fields except 'Class'
    for item in data:
        for key, value in item.items():
            if key != 'Class' and isinstance(value, str):
                try:
                    # Convert string to number (int or float)
                    if '.' in value:
                        item[key] = float(value)
                    else:
                        item[key] = int(value)
                except ValueError:
                    # If conversion fails, keep as string
                    pass
    
    # Write the converted data back to file
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
    
    print("Successfully converted all string numbers to actual numbers in data.json")
    print(f"Processed {len(data)} records")

if __name__ == "__main__":
    convert_string_numbers_to_numbers() 