from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "BI Report Automation Platform"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}