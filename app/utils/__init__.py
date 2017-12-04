from datetime import datetime, timedelta

def kenya_time():
    return datetime.utcnow() + timedelta(hours=4)