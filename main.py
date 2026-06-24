from fastapi import FastAPI, Depends

from app.auth import login
from app.deps import verify_token

from app.db import Base, engine
from app.db import SessionLocal
from app.models import Report, Notification

from app import models 

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"status": "API berhasil jalan"}

@app.post("/login")
def login_user(data: dict):
    return login(data["email"], data["password"])

@app.get("/profile")
def profile(user=Depends(verify_token)):
    return {
        "success": True,
        "message": "data user berhasil diakses",
        "data": user
    }
@app.get("/test-db")
def test_db():
    return {"message": "database test"}

@app.post("/reports")
def create_report(data: dict, user=Depends(verify_token)):

    db = SessionLocal()

    report = Report(
        email=user["email"],
        title=data["title"],
        description=data["description"]
    )

    db.add(report)
    db.commit()
    db.refresh(report)

    return {
        "success": True,
        "message": "laporan berhasil dibuat",
        "data": {
            "id": report.id,
            "title": report.title
        }
    }
    
@app.get("/reports")
def get_reports(user=Depends(verify_token)):

    db = SessionLocal()

    if user["role"] == "admin":
        reports = db.query(Report).all()

    else:
        reports = db.query(Report).filter(
            Report.email == user["email"]
        ).all()

    result = []

    for report in reports:
        result.append({
            "id": report.id,
            "email": report.email,
            "title": report.title,
            "description": report.description,
            "status": report.status
        })

    return {
        "success": True,
        "data": result
    }
    
@app.put("/reports/{report_id}/status")
def update_report_status(
    report_id: int,
    data: dict,
    user=Depends(verify_token)
):

    if user["role"] != "admin":
        return {
            "success": False,
            "message": "Access denied"
        }

    db = SessionLocal()

    report = db.query(Report).filter(
        Report.id == report_id
    ).first()

    if not report:
        return {
            "success": False,
            "message": "Report tidak ditemukan"
        }

    report.status = data["status"]

    notification = Notification(
        email=report.email,
        message=f"Status laporan '{report.title}' berubah menjadi {data['status']}"
    )

    db.add(notification)

    db.commit()

    return {
        "success": True,
        "message": "Status berhasil diupdate"
    }
    
@app.get("/notifications")
def get_notifications(user=Depends(verify_token)):

    db = SessionLocal()

    notifications = db.query(Notification).filter(
        Notification.email == user["email"]
    ).all()

    result = []

    for n in notifications:
        result.append({
            "id": n.id,
            "message": n.message
        })

    return {
        "success": True,
        "data": result
    }
    
@app.get("/dashboard/stats")
def dashboard_stats(user=Depends(verify_token)):

    if user["role"] != "admin":
        return {
            "success": False,
            "message": "Access denied"
        }

    db = SessionLocal()

    total_reports = db.query(Report).count()

    open_reports = db.query(Report).filter(
        Report.status == "open"
    ).count()

    resolved_reports = db.query(Report).filter(
        Report.status == "resolved"
    ).count()

    return {
        "success": True,
        "data": {
            "total_reports": total_reports,
            "open_reports": open_reports,
            "resolved_reports": resolved_reports
        }
    }