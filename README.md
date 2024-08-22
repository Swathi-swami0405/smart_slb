# smart_slb
PROBLEM STATEMENT:
Check for share name and alert percentage from input file. Go to nse official site. Get bid price and best offer price for the particular share name. Check if the bid percentage is greater than or equal to alert percentage. If yes, send a message saying "YOU HAVE A DEAL!"

PROBLEM APPROACH:
1. Fetch HTTP Response using GET method from url - "https://www.nseindia.com/get-quotes/slb?symbol={share_name}".
2. Extract cookies from the http response header.
3. Construct a http request by setting the cookies with "nseappid" and "nsit" and fetch http response from  https://www.nseindia.com/api/live-analysis-slb?symbol={share_name} using get method.
4. Parse the json data received in response and construct the alert based on the input data.

INPUT FORMAT:
Text file containing SHARENAME, ALERT_PERCENTAGE

OUTPUT FORMAT:
Deal/No Deal message.
