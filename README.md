# robotframework-awslib
AWSlib is a handy Robot Famework layer for interacting with, automating, and testing any AWS process in your AWS instance.


AWSlib is built on top of boto3 (and thus Botocore) which will handle session handling via a dynamic keyword API provided by this library. As such, AWSlib will use your default authentication credentials in ~/.aws/credentials.

This library is very much a work-in-progress but the idea is to eventually dynamically generate keywords from the metadata provided by boto3. This will give us the ability to use any resource in our account on the fly.

Additional handling and dynamic call-caching to eventually be provided by an implementation on top of the boto3 Event system, exposed through the meta object on the client or resource.
