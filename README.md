envois
======

Automated invoicing by Lambda Labs, Inc.

## Example 

```bash
./invoice invoice.json
```

Open the resulting HTML in a browser, save it as a PDF, give it to the people
who owe you money.

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
