from django.http import HttpResponseForbidden,HttpRequest



class LogMiddleware:
    def __init__(self,get_reponse):
        self.get_response = get_reponse
        
    
    def __call__(self,request: HttpRequest):
        print("Viewga kelishidan oldingi kod")
        if request.path == '/salom':
            return HttpResponseForbidden()
        
        response = self.get_response(request)
        print("Viewdan keyingi bajarilgan kod ")
        return response