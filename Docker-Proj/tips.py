# Renee Guldi
# February 18, 2024,
# DockerProject

import emoji


def calc_tip(bill_amount, tip_percent):
    tip_total = bill_amount * (tip_percent / 100)
    bill_total = bill_amount + tip_total
    return bill_total


def main():
    bill_amount = float(input("Enter bill amount after taxes: $"))
    tip_percent = float(input("Enter the tip % you would like to give (10%, 15%, 20%): "))

    bill_total = calc_tip(bill_amount, tip_percent)
    tip_total = bill_total - bill_amount

    print(f"Bill amount: ${bill_amount:.2f}")
    print(f"Tip amount: ${tip_total:.2f}")
    print(f"Total bill amount including tip: ${bill_total:.2f}")

    print(emoji.emojize(f"\nThank you for using this tip calculator! Bye! :waving_hand:"))


if __name__ == "__main__":
    main()
