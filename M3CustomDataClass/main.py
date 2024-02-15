# Renee Guldi
# SDEV220 - Python
# Prof. Chris Francis
# February 14, 2024

from guitar import guitar

def main():
    guitar1 = guitar("Fender", "Precision Bass", 4, "Orange")
    guitar2 = guitar("Gibson", "Les Paul", 6, "Red")
    
    print(guitar1 == guitar2)

if __name__ == "__main__":
    main()