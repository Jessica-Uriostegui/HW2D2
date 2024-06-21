# Jessica Uriostegui
# June 19,2024
# Lesson 3: Assignments | Sets

print()
print( "**Task 1: Flight Route Comparison**\n" )

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}


def similar():
    same = our_routes.intersection(competitor_routes)
    return same

def our_unique():
    unique =our_routes.difference(competitor_routes)
    return unique

def not_shared ():
    shared = our_routes.symmetric_difference(competitor_routes)
    return shared

def main ():

    same = similar()
    print(f"Destinations both airlines travel to: {same} ")

    unique = our_unique()
    print (f"Destinations that our airline only travels to: {unique}")

    shared = not_shared()
    print(f"Destinations that neither airline share: {shared}")

main ()
print()
#Set Operations in Data Analysis
print("Task: 1 Duplicate Entries Cleanup \n")
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
set_ids = set(customer_ids)
print(f"Here are the unique customer IDs: {set_ids}")

