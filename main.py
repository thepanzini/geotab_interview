#
def format_number(value):
    """Returns a number formatted with a suffix indicating amount.
    :param value: The number to format in either int or decimal format
    :type value: float
    :returns: A string containing the formatted number with decimal and suffix
    :rtype str
    """
    # Some good sanity checks
    # Check for string
    # Check for negative
    # Check for 0
    if value is None or isinstance(value, str) or value < 0:
        return formatted_error(value)
    # Less then 1M return number (999,999 and down)
    if value < 1000000:
        return formatted_output(value, value)

    suffix = ""

    # Check range between 1M and 1B
    if 1000000 <= value < 1000000000:
        suffix = "M"
    # Check range between 1B and 1T
    if 1000000000 <= value < 1000000000000:
        suffix = "B"
    # Check range over 1T for now...
    if 1000000000000 <= value:
        suffix = "T"

    val_str = str(value)
    # Check second digit indicating the need for a decimal
    if int(val_str[1]) != 0:
        # Needs decimal (1.1B)
        output = f"{val_str[0]}.{val_str[1]}{suffix}"
    else:
        # No decimal needed (1B)
        output = f"{val_str[0]}{suffix}"

    return formatted_output(value, output)


def formatted_output(value, output):
    """Returns a nicely formatted string describing the format change.
        :param value: The number input
        :type value: float
        :param output: The format output
        :type value: float
        :returns: A string containing the input transformation and the final output
        :rtype str
        """
    return f"Input Value: {value}\nOutput Format: {output}"


def formatted_error(value):
    """Returns a nicely formatted error message for why the formatting could not happen.
        :param value: The number input
        :type value: any
        :returns: A string containing the inputted number and error info
        :rtype str
        """
    check = type_check(value)
    return f"Input Value: '{value}' of type {check} is not an valid input and can not be formatted"


def type_check(value):
    """Returns a nice format of variable type.
        :param value: The value to check type of
        :returns: A string containing the type
        :rtype str
        """
    check = type(value)
    if check is str:
        return 'str'
    elif check is int:
        if value < 0:
            return 'int(negative)'
        return 'int'
    elif check is float:
        return 'int'
    else:
        return check


if __name__ == '__main__':
    print("TESTS:")
    # Provided Test Cases:
    # input: 1000000
    # output: 1M
    print(format_number(1000000))
    # input: 2500000.34
    # output: 2.5M
    print(format_number(2500000.34))
    # input: 532
    # output: 532
    print(format_number(532))
    # input: 1123456789
    # output: 1.1B
    print(format_number(1123456789))

    print("\nEXTRA TESTS:")
    # My additional Test Cases:
    # input: "1123456789"
    # output: 0
    print(format_number("1123456789"))
    # input: 1
    # output: 1
    print(format_number(1))
    # input: 0
    # output: 0
    print(format_number(0))
    # input: -1000000
    # output: 0
    print(format_number(-1000000))
    # input: 9999999999999
    # output: 9.9T
    print(format_number(9999999999999))
    # input: 90000000000000
    # output: 9T
    print(format_number(90000000000000))
