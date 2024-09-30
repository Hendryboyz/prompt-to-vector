from grpc import Server
from grpc_health.v1 import health
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc
import threading
from time import sleep

import prompt_to_vector


def _add_methods(grpc_server: Server) -> None:
    prompt_to_vector.add_server(grpc_server)

def _toggle_health(health_servicer: health.HealthServicer, service: str):
    next_status = health_pb2.HealthCheckResponse.SERVING
    while True:
        if next_status == health_pb2.HealthCheckResponse.SERVING:
            next_status = health_pb2.HealthCheckResponse.NOT_SERVING
        else:
            next_status = health_pb2.HealthCheckResponse.SERVING

        health_servicer.set(service, next_status)
        sleep(5)

def _configure_health_check(server: Server):
    health_servicer = health.HealthServicer(
        experimental_non_blocking=True,
    )
    health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)
    # Use a daemon thread to toggle health status
    toggle_health_status_thread = threading.Thread(
        target=_toggle_health,
        args=(health_servicer, 'helloworld.Greeter'),
        daemon=True,
    )
    toggle_health_status_thread.start()
