# Renee Guldi
# Feb 22, 2024
# M5- CI/CD Pipeline
# Payroll Calc


def calc_pay(hours_worked, pay_rate):
    gross_pay = hours_worked * pay_rate
    if hours_worked > 40:
        overtime_worked = hours_worked - 40
        overtime_pay = overtime_worked * (pay_rate * 1.5)
    else:
        overtime_pay = 0

    check_total = gross_pay + overtime_pay
    
    return check_total

def main():
    print("Welcome to our Payroll Calculator\n")

    hours_worked = float(input("Please input employee's worked hours: "))
    pay_rate = float(input("Please input employee's hourly rate: "))

    check_total = calc_pay(hours_worked, pay_rate)
    print(f"This employee's gross pay is: {check_total}")


if __name__ =="__main__":
    main()