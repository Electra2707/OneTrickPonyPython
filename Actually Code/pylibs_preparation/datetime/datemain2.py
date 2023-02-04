import datetime
gvr = datetime.date(1956, 1, 31)
gvr_format=gvr.strftime("%A, %B %d, %Y")

print(f"GVR was born on {gvr_format}")

print(f"GVR was born on {gvr:%A, %B %d, %Y}")

gvr_format = gvr.isoformat()
print(f"GVR was born on {gvr_format}")