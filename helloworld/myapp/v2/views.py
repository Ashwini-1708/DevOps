from django.http import HttpResponse #send simple text/html responses from a Django view.
from django.http import JsonResponse


from django.http import JsonResponse
import json

@csrf_exempt
def profile(request):
    if request.method == "GET":
        return JsonResponse({
            "version": "v2",
            "message": "Profile GET",
            "fields": ["username", "phone_number"]
        })

    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("username")
        phone_number = data.get("phone_number")

        if not username or not phone_number:
            return JsonResponse(
                {"error": "username and phone_number are required"},
                status=400
            )

        return JsonResponse({
            "version": "v2",
            "username": username,
            "phone_number": phone_number
        })
