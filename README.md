# Number Formatter

Number Formatter is a utility developed in python to format a number as part of an interview assessment for GeoTab.

## Installation

Clone this repository make sure your are using the latest version of python3

## Usage

Run the main file and see the output.

```bash
python3 main.py
```

## Approach

The way I chose to implement is to use the assumption that the input value was as number type (float, int, long)
I can then compare against number ranges to see if the provided input is in the million/billion/trillion, etc... range.
This will give me the proper suffix to use for the format.

Then to retrieve the decimal value I check the second number to see if it is zero.
If it is, then no decimal is needed. If not then add a `.`, grab the second number and add it to the output string.
This is made easier by python's treatment of strings as arrays.

## Assumptions

I assumed the input would be number type (float, int, long) that must be positive,
and that it would be less than 1 trillion.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
