import requests
import datetime
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import base64

class KalshiClient:
    def __init__(self, api_key_id: str, private_key_str: str):
        """
        Initialize Kalshi API client
        
        Args:
            api_key_id: Your Kalshi API Key ID
            private_key_str: Your private key as a string (from env variable)
        """
        self.api_key_id = api_key_id
        self.private_key = self._load_private_key_from_string(private_key_str)
        self.base_url = 'https://api.elections.kalshi.com'
        
    def _load_private_key_from_string(self, key_str: str):
        """Load private key from string"""
        # Add PEM headers if not present
        if not key_str.startswith('-----BEGIN'):
            key_str = f"-----BEGIN PRIVATE KEY-----\n{key_str}\n-----END PRIVATE KEY-----"
        
        private_key = serialization.load_pem_private_key(
            key_str.encode('utf-8'),
            password=None,
            backend=default_backend()
        )
        return private_key
    
    def _sign_message(self, message: str) -> str:
        """Sign a message with the private key using RSA-PSS"""
        signature = self.private_key.sign(
            message.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return base64.b64encode(signature).decode('utf-8')
    
    def _get_auth_headers(self, method: str, path: str) -> dict:
        """Generate authentication headers for a request"""
        # Get current timestamp in milliseconds
        timestamp = int(datetime.datetime.now().timestamp() * 1000)
        timestamp_str = str(timestamp)
        
        # Strip query parameters from path before signing
        path_without_query = path.split('?')[0]
        
        # Create message to sign: timestamp + method + path
        msg_string = timestamp_str + method + path_without_query
        
        # Sign the message
        signature = self._sign_message(msg_string)
        
        # Return headers
        return {
            'KALSHI-ACCESS-KEY': self.api_key_id,
            'KALSHI-ACCESS-SIGNATURE': signature,
            'KALSHI-ACCESS-TIMESTAMP': timestamp_str,
            'Content-Type': 'application/json'
        }
    
    def get_balance(self) -> dict:
        """Get account balance"""
        method = "GET"
        path = "/trade-api/v2/portfolio/balance"
        
        headers = self._get_auth_headers(method, path)
        response = requests.get(self.base_url + path, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"API Error: {response.status_code} - {response.text}")
    
    def get_portfolio(self) -> dict:
        """Get portfolio positions"""
        method = "GET"
        path = "/trade-api/v2/portfolio/positions"
        
        headers = self._get_auth_headers(method, path)
        response = requests.get(self.base_url + path, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"API Error: {response.status_code} - {response.text}")