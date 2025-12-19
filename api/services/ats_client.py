import requests
import os

BASE_URL = os.getenv("ATS_BASE_URL")
API_KEY = os.getenv("ATS_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def get_jobs():
    res = requests.get(f"{BASE_URL}/jobs", headers=HEADERS)
    res.raise_for_status()
    return res.json()

def create_candidate(data):
    res = requests.post(f"{BASE_URL}/candidates", json=data, headers=HEADERS)
    res.raise_for_status()
    return res.json()

def create_application(candidate_id, job_id):
    payload = {
        "candidate_id": candidate_id,
        "job_id": job_id
    }
    res = requests.post(f"{BASE_URL}/applications", json=payload, headers=HEADERS)
    res.raise_for_status()
    return res.json()

def get_applications(job_id):
    res = requests.get(
        f"{BASE_URL}/applications?job_id={job_id}",
        headers=HEADERS
    )
    res.raise_for_status()
    return res.json()
