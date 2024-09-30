import asyncio
import logging

from config import Settings
import grpc
from methods import _add_methods, _configure_health_check

_cleanup_coroutines = []  

async def serve() -> None:
    settings = Settings()
    
    logger = logging.getLogger('app')
    server = grpc.aio.server()
    _add_methods(server)
    _configure_health_check(server)
    listen_addr = f'[::]:{settings.port}'
    server.add_insecure_port(listen_addr)
    await server.start()
    logger.info(f'Starting server on {listen_addr}')
    
    async def server_graceful_shutdown():
        logging.info("Starting graceful shutdown...")
        # Shuts down the server with 5 seconds of grace period. During the
        # grace period, the server won't accept new connections and allow
        # existing RPCs to continue within the grace period.
        await server.stop(5)
    
    _cleanup_coroutines.append(server_graceful_shutdown())
    await server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.NOTSET,
        format='%(asctime)s - %(levelname)s[%(name)s]: %(message)s')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(serve())
    finally:
        loop.run_until_complete(*_cleanup_coroutines)
        loop.close()
    