from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services.ats_client import (
    get_jobs,
    create_candidate,
    create_application,
    get_applications
)

@api_view(["GET"])
def jobs(request):
    try:
        jobs = get_jobs()
        return Response(jobs)
    except Exception as e:
        return Response({"error": str(e)}, status=400)


@api_view(["POST"])
def candidates(request):
    try:
        candidate = create_candidate(request.data)

        application = create_application(
            candidate_id=candidate["id"],
            job_id=request.data["job_id"]
        )

        return Response({
            "candidate": candidate,
            "application": application
        }, status=201)

    except Exception as e:
        return Response({"error": str(e)}, status=400)


@api_view(["GET"])
def applications(request):
    try:
        job_id = request.GET.get("job_id")
        data = get_applications(job_id)
        return Response(data)
    except Exception as e:
        return Response({"error": str(e)}, status=400)
