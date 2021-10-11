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
    if value is None or isinstance(value, str):
        return 0
    # Less then 1M return number (999,999 and down)
    if value < 1000000:
        return value

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

    return output


if __name__ == '__main__':
    # Provided Test Cases:
    # input: 1000000
    # output: 1M
    # input: 2500000.34
    # output: 2.5M
    # input: 532
    # output: 532
    # input: 1123456789
    # output: 1.1B

    # My own test cases:
    # input: "1123456789"
    # output: 0
    # input: 0
    # output: 0
    print(format_number(1000000))
    print(format_number(2500000.34))
    print(format_number(532))
    print(format_number(1123456789))
    print(format_number("1123456789"))
    print(format_number(1))
