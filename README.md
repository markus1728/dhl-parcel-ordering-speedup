# DHL-Parcel-Ordering-Speedup
The ordering process of a simple DHL-Parcel requires quite a few steps, is very repetitive and also time-consuming. 
This script simplifies the whole process. 

# Usage 

Deposit the sender's address in the init-method.

```python
 def __init__(self):
        super().__init__()

        # Insert the sender address details
        self.sender_first_name = "Max"
        self.sender_second_name = "Mustermann"
        self.sender_street = "Musterallee"
        self.sender_street_number = "10"
        self.sender_postal_code = "60318"
        self.sender_city = "Frankfurt"
        self.sender_email = "max.mustermann@gmx.com"
```

The user can insert the receiver's address and click the desired parcel-form. 
Afterwards the program navigates through the DHL-Websites, clicks the relevant buttons and and fills out the necessary fields.
In the end the user can confirm and buy his order with one click. 
