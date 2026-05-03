#!/usr/bin/env python3
import os

# Get student name from environment variable, default to "Hrithik"
student_name = os.environ.get('STUDENT_NAME', 'Hrithik').title()

print("Message: Hello MLOps!")
print(f"Brought to you by : {student_name}")
