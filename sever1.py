import grpc
import asyncio
from concurrent import futures
import chat_pb2
import chat_pb2_grpc
import logging

# Setup logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ChatService(chat_pb2_grpc.ChatServiceServicer):
    async def ChatStream(self, request_iterator, context):
        """Handles bidirectional streaming chat messages"""
        async for request in request_iterator:
            logger.info(f"Received message from {request.sender}: {request.message}")
            yield chat_pb2.ChatMessage(sender="Server", message=f"Echo: {request.message}")

async def serve():
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatService(), server)
    
    server_address = "0.0.0.0:50051"  # Accessible from Docker and network
    server.add_insecure_port(server_address)
    logger.info(f"Starting gRPC server on {server_address}...")
    
    await server.start()
    await server.wait_for_termination()

if __name__ == "__main__":
    asyncio.run(serve())
