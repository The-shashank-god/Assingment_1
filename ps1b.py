'''
Assignment 1 part B
Name: P shashank
prn : 250200465
application :CDS/2025/0987
Collaborators: B naga maheswar reddy
'''
# inputs
annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# constants
down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04
months = 0

# loop until enough savings
while current_savings < down_payment:

    # interest added every month
    current_savings += current_savings * (r / 12)

    # monthly saving added
    current_savings += (annual_salary / 12) * portion_saved

    months += 1

    # every 6 months salary increases
    if months % 6 == 0:
        annual_salary += annual_salary * semi_raise

# output
print("Number of months:", months)
