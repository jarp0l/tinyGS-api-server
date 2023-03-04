import uvicorn

from app.utils.config import CONFIG

if __name__ == "__main__":
    uvicorn.run("routes:app", host="0.0.0.0", port=CONFIG.server_port, reload=True)
