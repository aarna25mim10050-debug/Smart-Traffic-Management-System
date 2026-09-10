# SMART TRAFFIC MANAGEMENT SYSTEM
import random

# TRAFFIC DATA


roads = {
    "Road A": {
        "vehicles": 0,
        "emergency": False
    },

    "Road B": {
        "vehicles": 0,
        "emergency": False
    },

    "Road C": {
        "vehicles": 0,
        "emergency": False
    },

    "Road D": {
        "vehicles": 0,
        "emergency": False
    }
}

# MODULE 1: ENTER VEHICLE COUNTS

def enter_vehicle_count():

    print("\n========== ENTER TRAFFIC DATA ==========")

    for road in roads:

        while True:

            try:

                count = int(
                    input("Enter number of vehicles on "
                          + road + ": ")
                )

                if count < 0:

                    print("Vehicle count cannot be negative.")
                    continue

                roads[road]["vehicles"] = count

                break

            except ValueError:

                print("Please enter a valid number.")


    print("\nTraffic data updated successfully!")


# MODULE 2: SIMULATE RANDOM TRAFFIC

def simulate_traffic():

    print("\n========== TRAFFIC SIMULATION ==========")

    for road in roads:

        # Generate a random number between 0 and 50
        vehicles = random.randint(0, 50)

        roads[road]["vehicles"] = vehicles

        print(
            road,
            "->",
            vehicles,
            "vehicles"
        )


    print("\nTraffic simulation completed!")


# MODULE 3: TRAFFIC ANALYSIS

def get_traffic_level(vehicles):

    if vehicles <= 10:

        return "LOW"

    elif vehicles <= 25:

        return "MEDIUM"

    else:

        return "HIGH"


def analyze_traffic():

    print("\n========== TRAFFIC ANALYSIS ==========")

    for road in roads:

        vehicles = roads[road]["vehicles"]

        level = get_traffic_level(vehicles)

        print(
            road,
            "| Vehicles:",
            vehicles,
            "| Traffic Level:",
            level
        )


# MODULE 4: CALCULATE SIGNAL TIME
def calculate_signal_time(vehicles):

    if vehicles <= 10:

        return 15

    elif vehicles <= 25:

        return 30

    else:

        return 45


# MODULE 5: SMART TRAFFIC SIGNAL CONTROL

def control_signal():

    print("\n========== SMART SIGNAL CONTROL ==========")

    # First check for emergency vehicles

    for road in roads:

        if roads[road]["emergency"] == True:

            print("\n🚨 EMERGENCY VEHICLE DETECTED!")

            print(
                "Priority given to:",
                road
            )

            print(
                "GREEN SIGNAL:",
                road
            )

            print(
                "Green Signal Time: 60 seconds"
            )


            # All other roads get red
            for other_road in roads:

                if other_road != road:

                    print(
                        "RED SIGNAL:",
                        other_road
                    )


            return

    # Find the road with the highest number of vehicles

    selected_road = max(
        roads,
        key=lambda road: roads[road]["vehicles"]
    )


    vehicle_count = roads[selected_road]["vehicles"]


    # Calculate green signal time
    green_time = calculate_signal_time(
        vehicle_count
    )


    print("\n========== SIGNAL RESULT ==========")

    print(
        "Selected Road:",
        selected_road
    )

    print(
        "Vehicle Count:",
        vehicle_count
    )

    print(
        "Green Signal Time:",
        green_time,
        "seconds"
    )


    # Display signals for all roads
    print("\nTraffic Signals:")

    for road in roads:

        if road == selected_road:

            print(
                "🟢 GREEN:",
                road
            )

        else:

            print(
                "🔴 RED:",
                road
            )


# MODULE 6: EMERGENCY VEHICLE

def set_emergency():

    print("\n========== EMERGENCY VEHICLE ==========")

    print("Available Roads:")

    for road in roads:

        print("-", road)


    road_name = input(
        "\nEnter road with emergency vehicle: "
    )


    if road_name not in roads:

        print("\nInvalid road name!")

        return


    # Remove emergency status from all roads
    for road in roads:

        roads[road]["emergency"] = False


    # Give emergency status to selected road
    roads[road_name]["emergency"] = True


    print(
        "\n🚨 Emergency vehicle registered on",
        road_name
    )

    print(
        "This road will receive priority."
    )

# MODULE 7: CLEAR EMERGENCY

def clear_emergency():

    for road in roads:

        roads[road]["emergency"] = False


    print(
        "\nEmergency status cleared successfully!"
    )


# MODULE 8: TRAFFIC REPORT

def traffic_report():

    print("\n========== TRAFFIC REPORT ==========")


    total_vehicles = 0


    # Calculate total vehicles
    for road in roads:

        vehicles = roads[road]["vehicles"]

        total_vehicles = (
            total_vehicles + vehicles
        )


    # Find busiest road
    busiest_road = max(
        roads,
        key=lambda road: roads[road]["vehicles"]
    )


    # Display individual road information
    print("\nRoad-wise Traffic:")

    for road in roads:

        vehicles = roads[road]["vehicles"]

        level = get_traffic_level(
            vehicles
        )

        print(
            road,
            "->",
            vehicles,
            "vehicles |",
            level
        )


    print("\n----------------------------")

    print(
        "Total Vehicles:",
        total_vehicles
    )

    print(
        "Busiest Road:",
        busiest_road
    )

    print(
        "Vehicles on Busiest Road:",
        roads[busiest_road]["vehicles"]
    )

# MODULE 9: MAIN MENU

def main():

    while True:

        print("\n")
        print("==========================================")
        print("     SMART TRAFFIC MANAGEMENT SYSTEM")
        print("==========================================")

        print("1. Enter Vehicle Counts")
        print("2. Simulate Random Traffic")
        print("3. Analyze Traffic")
        print("4. Control Traffic Signal")
        print("5. Emergency Vehicle Priority")
        print("6. Clear Emergency Status")
        print("7. Generate Traffic Report")
        print("8. Exit")


        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            enter_vehicle_count()

        elif choice == "2":

            simulate_traffic()
        elif choice == "3":

            analyze_traffic()

        elif choice == "4":

            control_signal()
        elif choice == "5":

            set_emergency()

        elif choice == "6":

            clear_emergency()

        elif choice == "7":

            traffic_report()

        elif choice == "8":

            print(
                "\nThank you for using "
                "Smart Traffic Management System!"
            )

            break
        else:

            print(
                "\nInvalid choice!"
                " Please select a number from 1 to 8."
            )


# START PROGRAM

main()
