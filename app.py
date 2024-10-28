#!/usr/bin/env python3
import os
import json
import argparse
import aws_cdk as cdk

from course_status.course_status_stack import CourseStatusStack

choice = input("Deployment envionment [1 for staging, 2 for production]: ")

if choice == 2:
  environment = "production"
else:
  environment = "staging" # default is staging

print("Environment: " + environment)

app = cdk.App()

try:
  with open('config.json') as config_file:
    settings = json.load(config_file)

  CourseStatusStack(app, 
                  "CourseStatus-" + settings[environment]["suffix"],
                  settings[environment]["prefix"],
                  settings[environment]["suffix"],
                  env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))
                )

  app.synth()

except Exception as e:
  print(f"Error reading config file: {e}")

