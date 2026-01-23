def find_train_set(carriage_number):
    # convert to string and strip whitespace
    carriage = str(carriage_number).strip().upper()

    # carriage type definitions
    carriage_types = {
        # D sets - 4 car mariyung
        'DD97': {'type': 'driving trailer', 'cars': 4, 'prefix': 'D', 'name': 'mariyung'},
        'DN85': {'type': 'non-driving motor', 'cars': 4, 'prefix': 'D', 'name': 'mariyung'},
        'DND83': {'type': 'non-driving motor', 'cars': 4, 'prefix': 'D', 'name': 'mariyung'},
        'DDA93': {'type': 'driving trailer (atp)', 'cars': 4, 'prefix': 'D', 'name': 'mariyung'},

        # D sets - 6 car mariyung
        'DD98': {'type': 'driving trailer', 'cars': 6, 'prefix': 'D1', 'name': 'mariyung'},
        'DNL88': {'type': 'non-driving motor', 'cars': 6, 'prefix': 'D1', 'name': 'mariyung'},
        'DT96': {'type': 'non-driving trailer', 'cars': 6, 'prefix': 'D1', 'name': 'mariyung'},
        'DN86': {'type': 'non-driving motor', 'cars': 6, 'prefix': 'D1', 'name': 'mariyung'},
        'DND84': {'type': 'non-driving motor', 'cars': 6, 'prefix': 'D1', 'name': 'mariyung'},
        'DDA94': {'type': 'driving trailer (atp)', 'cars': 6, 'prefix': 'D1', 'name': 'mariyung'},

        # H sets - 4 car oscar
        'OD69': {'type': 'driving trailer', 'cars': 4, 'prefix': 'H', 'name': 'oscar'},
        'ONL59': {'type': 'non-driving motor with lavatory', 'cars': 4, 'prefix': 'H', 'name': 'oscar'},
        'ONL58': {'type': 'non-control motor with lavatory', 'cars': 4, 'prefix': 'H', 'name': 'oscar'},
        'ON59': {'type': 'non-control motor', 'cars': 4, 'prefix': 'H', 'name': 'oscar'},
        'ON58': {'type': 'non-control motor', 'cars': 4, 'prefix': 'H', 'name': 'oscar'},
    }

    # extract the numeric part
    try:
        # find matching carriage type
        matched_type = None
        for prefix, info in carriage_types.items():
            if carriage.startswith(prefix):
                matched_type = info
                break

        if not matched_type:
            return None, "carriage number pattern not recognised :("

        # calculate set number based on carriage number
        set_num = None

        # oscar calculation logic
        if carriage.startswith('OD69'):
            carriage_num = int(carriage[4:])
            # special cases first
            if carriage_num == 6921 or carriage_num == 6922:
                set_num = 49
            # H1-10: OD69(n*2-1) - odd numbers 1-19
            elif carriage_num % 2 == 1 and carriage_num <= 19:
                set_num = (carriage_num + 1) // 2
            # H11-48: OD69(n*2+1) - odd numbers 21-95
            elif carriage_num % 2 == 1 and carriage_num >= 21 and carriage_num <= 95:
                set_num = (carriage_num - 1) // 2
            # H50-55: OD69(n*2-57) - even numbers 43-53
            elif carriage_num % 2 == 0 and carriage_num >= 43 and carriage_num <= 53:
                set_num = (carriage_num + 57) // 2

        elif carriage.startswith('ONL599'):
            # special case H49
            set_num = 49
        elif carriage.startswith('ONL59'):
            carriage_num = int(carriage[5:])
            # H1-48: ONL59(n+50)
            set_num = carriage_num - 50
        elif carriage.startswith('ONL58'):
            carriage_num = int(carriage[5:])
            # H50-55: ONL58(n+21)
            set_num = carriage_num - 21

        elif carriage.startswith('ON594'):
            # Special case H49
            if carriage == 'ON5949':
                set_num = 49
        elif carriage.startswith('ON59'):
            carriage_num = int(carriage[4:])
            # H1-48: ON59(n)
            set_num = carriage_num
        elif carriage.startswith('ON58'):
            carriage_num = int(carriage[4:])
            # H50-55: ON58(n-29)
            set_num = carriage_num + 29

        # d sets - just get last 2 digits
        elif carriage.startswith('D'):
            set_num = carriage[-2:]

        if set_num is None:
            return None, "could not calculate set number"

        # format the set number
        if matched_type['prefix'] == 'H':
            formatted_set = f"H{set_num:02d}"
        else:
            formatted_set = f"{matched_type['prefix']}{set_num}"

        return carriage.lower(), f"{matched_type['type']}", f"{formatted_set} ({matched_type['cars']} car {matched_type['name']})"

    except (IndexError, ValueError) as e:
        return None, f"error parsing carriage number: {e}"


def main():
    print("=" * 50)
    print("nsw train set identifier")
    print("=" * 50)
    print("enter 'f' at any time to finish")

    while True:
        carriage = input("enter the carriage number: ").strip()

        if carriage.lower() == 'f':
            print("keep on keeping on")
            break

        if not carriage:
            print("please enter the carriage number\n")
            continue

        result = find_train_set(carriage)

        if result[0]:
            print(f"    carriage number: {result[0]} - {result[1]}")
            print(f"    set number: {result[2]}")
        else:
            print(f"    {result[1]}")
        print()


if __name__ == "__main__":
    main()
