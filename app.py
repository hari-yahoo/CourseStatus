#!/usr/bin/env python3
import os

import aws_cdk as cdk

from course_status.course_status_stack import CourseStatusStack


app = cdk.App()

CourseStatusStack(app, 
                  "CourseStatusStaging",
                  env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
                  #env=cdk.Environment(account='123456789012', region='us-east-1'),
                )

app.synth()
