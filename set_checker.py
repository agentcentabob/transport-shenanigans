def find_train_set(carriage_number):
    """
    Determines the train set number from a carriage number.
    
    Patterns:
    - 4-car sets: DD97xx, DN85xx, DND83xx, DDA93xx
    - 6-car sets: DD98xx, DNL88xx, DT96xx, DN86xx, DND84xx, DDA94xx
    - 6-car sets have prefix '1' added to set number (e.g., D121)
    """
    
    # Convert to string and strip whitespace
    carriage = str(carriage_number).strip().upper()
    
    # Check if it starts with expected prefixes
    if not any(carriage.startswith(prefix) for prefix in ['DD', 'DN', 'DT', 'DDA']):
        return "Invalid carriage number format"
    
    # Extract the numeric part (last 2 digits are the set number)
    try:
        # Get the last 2 digits
        set_num = carriage[-2:]
        
        # Determine carriage type and whether it's 4-car or 6-car
        if carriage.startswith('DD97'):
            # Driving Trailer, 4-car
            return f"D{set_num} (4-car set)"
        
        elif carriage.startswith('DD98'):
            # Driving Trailer, 6-car
            return f"D1{set_num} (6-car set)"
        
        elif carriage.startswith('DNL88'):
            # Non-driving Motor, 6-car
            return f"D1{set_num} (6-car set)"
        
        elif carriage.startswith('DT96'):
            # Non-driving Trailer, 6-car
            return f"D1{set_num} (6-car set)"
        
        elif carriage.startswith('DN85'):
            # Non-driving Motor, 4-car
            return f"D{set_num} (4-car set)"
        
        elif carriage.startswith('DN86'):
            # Non-driving Motor, 6-car
            return f"D1{set_num} (6-car set)"
        
        elif carriage.startswith('DND83'):
            # Non-driving Motor, 4-car
            return f"D{set_num} (4-car set)"
        
        elif carriage.startswith('DND84'):
            # Non-driving Motor, 6-car
            return f"D1{set_num} (6-car set)"
        
        elif carriage.startswith('DDA93'):
            # Driving Trailer, 4-car
            return f"D{set_num} (4-car set)"
        
        elif carriage.startswith('DDA94'):
            # Driving Trailer, 6-car
            return f"D1{set_num} (6-car set)"
        
        else:
            return "Carriage number pattern not recognized"
            
    except (IndexError, ValueError):
        return "Error parsing carriage number"


def main():
    print("=" * 50)
    print("D SET TRAIN SET NUMBER FINDER")
    print("=" * 50)
    print()
    
    while True:
        carriage = input("Enter carriage number (or 'q' to quit): ").strip()
        
        if carriage.lower() == 'q':
            print("Goodbye!")
            break
        
        if not carriage:
            print("Please enter a carriage number.\n")
            continue
        
        result = find_train_set(carriage)
        print(f"➜ Train Set: {result}")
        print()


if __name__ == "__main__":
    main()