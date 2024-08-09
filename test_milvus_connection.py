from pymilvus import connections
from pymilvus.exceptions import MilvusException


def test_milvus_connection(host, port):
    try:
        connections.connect(
            alias="default",
            host=host,
            port=port,
            secure=False
        )
        print("Successfully connected to Milvus server!")

        from pymilvus import utility
        print(f"Milvus server version: {utility.get_server_version()}")

        connections.disconnect("default")
        print("Disconnected from Milvus server.")
    except MilvusException as e:
        print(f"Failed to connect to Milvus server. Error: {e}")


if __name__ == "__main__":
    milvus_host = "127.0.0.1" # 替換為你的 Milvus 容器 IP
    milvus_port = "19530"
    test_milvus_connection(milvus_host, milvus_port)
