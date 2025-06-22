import uvicorn


def start_server():
    uvicorn.run(
        "api.server:app",
        host="0.0.0.0",
        port=8123,
        reload=True,
    )


start_server()
