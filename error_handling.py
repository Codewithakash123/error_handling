import logging

logging.basicConfig(
    filename = "error.log",
    level = logging.ERROR
)

print("Program Started\n")

try:
    a = int(input("Enter The First Number:"))
    b = int(input("Enter The Second Number:"))

    result = a / b
    print("Result:",result)

except ZeroDivisionError:
    logging.error("Dividing by zero")
    print("Error: Don't divide by zero")

except ValueError:
    logging.error("Entered value is not a integer")
    print("Error: Enter a valid number")

except Exception as e:
    logging.error(e)
    print("Some error occured")

else:
    print("calculation successful")

finally:
    print("Program finished")



