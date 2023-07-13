
from src.configs.global_params import BASE_URL
from playwright.async_api import APIRequestContext,APIResponse

class PlatformAPI :
    def __init__(self, api_context: APIRequestContext) -> None:
        self.api_context = api_context
    
    async def post_api(self, request_endpoint: str, request_data: any, expected_status:int, expected_status_text: str):
        response: APIResponse = self.api_context.post(url= f"{BASE_URL}{request_endpoint}",
                                          data=request_data,
                                          headers={'Content-Type': 'application/x-www-form-urlencoded'})
        
        assert response.status == expected_status
        assert response.status_text == expected_status_text

    
    async def get_page_info(self, request_endpoint: str, expected_status: int, expected_status_text: str):
        response : APIResponse = self.api_context.get(url=f"{BASE_URL}{request_endpoint}")
        assert response.status == expected_status
        assert response.status_text == expected_status_text

        
        
        
