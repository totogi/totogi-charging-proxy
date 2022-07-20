# The Totogi Charging Proxy

In order to send requests to the Totogi Charger from a frontend application we made an easy-to-use proxy that will forward charging requests to the charger.

This proxy uses HTTP2 with the Python HTTPX library. It takes an fairly unopinionated approach to forwarding these requests. The only checks or modifications it performs are:

1. Checking that the expected charging URL is present in the forwarded request 
2. Assembling the headers for the request

The frontend system, in this case [The Totogi Emulator](https://github.com/totogi/emulator.totogidemos.com) must structure the requests as needed.
