@csrf_exempt

def profile(request):
    if request.method == "GET":
        return JsonResponse({
            "version": "v1",
            "message": "Profile GET",
            "fields": ["username", "age"]
        })

    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("username")
        age = data.get("age")

        if not username or not age:
            return JsonResponse(
                {"error": "username and age are required"},
                status=400
            )

        return JsonResponse({
            "version": "v1",
            "username": username,
            "age": age
        })
