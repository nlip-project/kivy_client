import httpx

'''
A very basic client for NLIP. 
The current version only sends one text message using NLIP.
It is intended as an early way to test the client
'''

def get_response(server_host:str, server_port:int, req:str):
    url = f'http://{server_host}:{server_port}/nlip'
    data = {
        'control':False,
        'format':'text',
        'subformat':'english',
        'content': req,
    }
    try:
        resp = httpx.post(url, json=data, timeout=120.0, follow_redirects=True)
        data = resp.raise_for_status().json()
        return data['content']
    except Exception as e:
        return(f'An Exception happened when talking to server -- {e}')
    
