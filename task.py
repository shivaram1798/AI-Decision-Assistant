from logic import *

# Defining symbols
rain = Symbol("rain")
heavy_traffic = Symbol("heavy_traffic")
early_meeting = Symbol("early_meeting")
strike = Symbol("strike")
appointment = Symbol("appointment")
road_construction = Symbol("road_construction")
work_from_home = Symbol("work_from_home")
drive = Symbol("drive")
public_transport = Symbol("public_transport")

# Defining knowledge base with additional rules
knowledge = And(
    Implication(Or(rain, early_meeting, strike), work_from_home),
    Implication(And(Not(rain), Not(heavy_traffic), Not(early_meeting), Not(road_construction)), drive),
    Implication(And(Not(strike), Not(rain)), public_transport),
    Implication(And(heavy_traffic, Not(rain), Not(early_meeting)), drive),
    Implication(appointment, drive),  #  Drive if there's an appointment
    Implication(And(road_construction, Not(appointment)), Not(drive)),  # Avoid driving with road construction unless there's an appointment
)

# Defining model checking queries
query1 = Implication(Not(rain), drive)
query2 = Implication(And(rain, heavy_traffic), work_from_home)
query3 = Implication(And(Not(strike), Not(rain)), public_transport)

# Perforing model check
print("--------------model check-----------------")
print("query 1", end='-')
print(model_check(knowledge, query1))
print("query 2", end='-')
print(model_check(knowledge, query2))
print("query 3", end='-')
print(model_check(knowledge, query3))
print("-------------------------------")

# Scenario 1: It's raining, and there's heavy traffic
scenario1 = And(rain, heavy_traffic)
print("scenario 1", end='-')
print(model_check(knowledge, Implication(scenario1, work_from_home)))  

# Scenario 2: There's a public transport strike, and it's not raining
scenario2 = And(strike, Not(rain))
print("scenario 2 (drive) ", end='-')
print(model_check(knowledge, Implication(scenario2, drive)))
print("scenario 2 (work_from_home)", end='-')
print(model_check(knowledge, Implication(scenario2, work_from_home)))  

# Scenario 3: There's no rain, traffic is light, and there's no strike
scenario3 = And(Not(rain), Not(heavy_traffic), Not(strike))
print("scenario 3 (drive) ", end='-')
print(model_check(knowledge, Implication(scenario3, drive)))
print("scenario 3 (public_transport) ", end='-')
print(model_check(knowledge, Implication(scenario3, public_transport)))  

# Scenario 4: You have a doctor's appointment
scenario4 = appointment
print("scenario 4", end='-')
print(model_check(knowledge, Implication(scenario4, drive)))  

# Scenario 5: There's road construction
scenario5 = And(road_construction, Not(appointment))
print("scenario 5", end='-')
print(model_check(knowledge, Implication(scenario5, Not(drive))))