PARTNER_CONFIG = {
    "acme": {
        "partner_code": "ACME",
        "delimiter": "|",
        "column_mapping": {
            "MBI": "external_id",
            "FNAME": "first_name",
            "LNAME": "last_name",
            "DOB": "dob",
            "EMAIL": "email",
            "PHONE": "phone"
        },
        "date_format": "%m/%d/%Y"
    },
    "bettercare": {
        "partner_code": "BETTERCARE",
        "delimiter": ",",
        "column_mapping": {
            "subscriber_id": "external_id",
            "first_name": "first_name",
            "last_name": "last_name",
            "date_of_birth": "dob",
            "email": "email",
            "phone": "phone"
        },
        "date_format": "%Y-%m-%d"
    }
}

