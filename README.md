envois
======

Automated invoicing by Lambda Labs, Inc.

## Requirements
- jinja2
- pdflatex (if generating pdfs from latex template)

## Example 

Currently the envois script and example json file exist in the
scripts directory. 

```bash
./scripts/envois <scripts/test.json 
```

or

```bash
./scripts/envois -f scripts/test.json 
```

Open the resulting HTML in a browser, save it as a PDF, give it to the people
who owe you money.

For more options on how to use envois:

```bash
usage: envois [-h] [-f INPUT_FILE] [-l] [-o OUTPUT_FILE]

optional arguments:
  -h, --help            show this help message and exit
  -f INPUT_FILE, --file INPUT_FILE
                        the json file used to generate invoice
  -l, --latex           use latex template to render invoice, default is to
                        use html
  -o OUTPUT_FILE        output file name, default is printing to stdout
```

### Example invoice file

```json
{
    "seller": {
        "name": "Lambda Labs, Inc.",
        "address": {
            "street": "857 Clay St. Suite 206",
            "city": "San Francisco",
            "state": "CA",
            "zip": "94108",
	    "email": "some@email.com",
	    "phone": "(555) 555-5555"
        },
        "account": {
            "swift": "...",
            "number": "...",
            "name": "Lambda Labs Inc.",
            "same_address": true
        }
    },
    "buyer": {
        "name": "Foo Corp",
        "address": {
            "street": "88 Foo Road, Foo Place",
            "city": "Fooville",
            "state": "BA",
            "zip": "31337"
        },
        "logo": "http://lambdal.com/images/lambda-labs-logo.png"
    },
    "items": [
        {
            "description": "Facial Detection & Landmark Recognition Perpetual License",
            "qty": 1,
            "unit_price": 32768.00
        }
    ],
    "terms": {
        "days": 30,
        "string": ""
    }
}
```

## Generated invoice contents

- Your company's logo
- Your company's address
- Your company's billing information
- Invoice date
- Invoice number
- Description and qty of goods
- Terms: NET X DAYS "INTEREST CHARGE ASSESSED ON BALANCES OVER X DAYS"

## LaTeX rendering options

Note: LaTeX invoice template taken from [www.latextemplates.com]
