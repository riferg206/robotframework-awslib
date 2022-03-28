import boto3


def get_boto3_session(**kwargs):
    boto3.Session(**kwargs).get_credentials()
    return boto3.Session(**kwargs)


def list_available_services(session):
    return session.get_available_services()


def list_service_methods(session, service):
    aws_service = session.client(f'{service.lower()}')
    service_methods = aws_service.meta.method_to_api_mapping
    return service_methods


#: boto3 extensibility features to be built out later, just fill out this function
def _registered_handler(params, **kwargs):
    pass


def invoke_operation(session, service, operation, config_params):
    aws_service = session.client(service)
    event_system = aws_service.meta.events
    api_operation = operation.replace("_", " ").title().replace(" ", "")
    try:
        event_system.register(f'provide-client-params.{service}.{api_operation}', _registered_handler)
        op_response = getattr(aws_service, operation)(**config_params)
    except Exception as e:
        raise e
