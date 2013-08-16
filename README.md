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
            "zipcode": "94108",
            "email": "enterprise@lambdal.com",
            "phone": "(555) 555-5555"
        },
        "account": {
            "bank": "...",
            "swift": "...",
            "number": "...",
            "name": "Lambda Labs Inc.",
            "same_address": false,
            "address": {
                "street": "...",
                "city": "...",
                "state": "...",
                "zipcode": "..."
            }
        },
        "logo": "http://lambdal.com/images/lambda-labs-logo.png"
    },
    "buyer": {
        "name": "...",
        "address": {
            "street": "...",
            "city": "...",
            "state": "...",
            "zipcode": "..."
        }
    },
    "items": [
        {
            "description": "Facial Detection & Landmark Recognition Perpetual License",
            "qty": 1,
            "unit_price": 65536.00
        }
    ],
    "terms": {
        "days": 0,
        "string": "Due upon receipt."
    },
    "date_of_purchase": "2013-07-01",
    "purchase_order_no": "0000-000-0000",
    "job_no": "..."
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
