from pymilvus import connections
from pymilvus.exceptions import MilvusException
from pymilvus import utility


def test_milvus_connection(host, port, collection):
    try:
        connections.connect(
            alias="default",
            host=host,
            port=port,
            secure=False
        )
        print("Step 1. Connected to Milvus server!")

        print(f"Step 2. Check Milvus server version ({utility.get_server_version()})")

        connections.connect(collection)
        print(f"Step 3. Connected to Milvus collection '{collection}'")
    except MilvusException as e:
        print(f"Failed to connect to Milvus server. Error: {e}")


if __name__ == "__main__":
    milvus_host = "127.0.0.1"
    milvus_port = "19530"
    milvus_collection = "default"
    test_milvus_connection(milvus_host, milvus_port, milvus_collection)
