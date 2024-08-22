import requests

def fetch_and_use_cookies(share_name):
    # Step 1: Fetch HTTP Response using GET method
    url_1 = f'https://www.nseindia.com/get-quotes/slb?symbol={share_name}'
    response_1 = requests.get(url_1)
    
    # Step 2: Extract cookies from the HTTP response header
    cookies = response_1.cookies
    nseappid = cookies.get('nseappid')
    nsit = cookies.get('nsit')
    
    # Check if the required cookies are present
    if not nseappid or not nsit:
        raise ValueError("Required cookies 'nseappid' or 'nsit' not found in the response.")
    
    # Step 3: Construct a HTTP request by setting the cookies
    url_2 = f'https://www.nseindia.com/api/live-analysis-slb?symbol={share_name}'
    cookies_dict = {'nseappid': nseappid, 'nsit': nsit}
    response_2 = requests.get(url_2, cookies=cookies_dict)
    
    # Step 4: Save the JSON response in a variable
    json_response = response_2.json()
    
    return json_response

# Example usage
share_name = 'HDFCBANK'
json_data = fetch_and_use_cookies(share_name)
print(json_data)
