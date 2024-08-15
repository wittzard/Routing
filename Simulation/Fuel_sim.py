import simpy
import random

# Constants
FUEL_TANK_SIZE = 50       # Maximum fuel tank size of vehicles
FUEL_PUMP_CAPACITY = 5    # Number of fuel pumps at the station
FUEL_PUMP_RATE = 2        # Fueling rate (liters per second)
VEHICLE_ARRIVAL_INTERVAL = 10  # Interval between vehicle arrivals (seconds)
SIM_TIME = 100            # Simulation time (seconds)

def vehicle(name, env, fuel_station, fuel_needed):
    """Vehicle process. Arrives at the fuel station, gets fuel, and leaves."""
    print(f'{name} arriving at fuel station at {env.now:.2f} seconds with {fuel_needed} liters needed')
    with fuel_station.request() as request:
        yield request
        print(f'{name} starting to fuel at {env.now:.2f} seconds')
        fueling_time = fuel_needed / FUEL_PUMP_RATE
        yield env.timeout(fueling_time)
        print(f'{name} leaving the fuel station at {env.now:.2f} seconds')

def vehicle_generator(env, fuel_station):
    """Generate vehicles arriving at the fuel station."""
    i = 0
    while True:
        yield env.timeout(random.expovariate(1.0 / VEHICLE_ARRIVAL_INTERVAL))
        fuel_needed = random.uniform(5, FUEL_TANK_SIZE)
        env.process(vehicle(f'Vehicle {i}', env, fuel_station, fuel_needed))
        i += 1

# Setup and start the simulation
random.seed(42)
env = simpy.Environment()

# Create the fuel station with a limited number of pumps
fuel_station = simpy.Resource(env, FUEL_PUMP_CAPACITY)

# Start the vehicle generator process
env.process(vehicle_generator(env, fuel_station))

# Run the simulation
env.run(until=SIM_TIME)
