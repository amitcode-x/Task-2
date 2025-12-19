from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import uuid

@csrf_exempt
def jobs(request):
    return JsonResponse([
        {
            "id": "job-1",
            "title": "Python Developer",
            "location": "Bangalore",
            "status": "OPEN",
            "external_url": "https://ats.fake/job-1"
        }
    ], safe=False)


@csrf_exempt
def candidates(request):
    if request.method == "POST":
        return JsonResponse({
            "id": str(uuid.uuid4())
        })
    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def applications(request):
    return JsonResponse([
        {
            "id": "app-1",
            "candidate_name": "Amit Chauhan",
            "email": "amit@gmail.com",
            "status": "APPLIED"
        }
    ], safe=False)
