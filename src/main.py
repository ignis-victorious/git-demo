#  ___________________
#  Import LIBRARIES
from fastapi import FastAPI
#  Import FILES
#  ___________________


app: FastAPI = FastAPI()


@app.get("/")
def hello(name: str = "World") -> str:
    return f"Hello, {name}!"


# @app.get("/goodbye")
# def goodbye(name: str = "World") -> str:
#     return f"Goodbye, {name}!"


@app.get("/goodbye")
def goodbye() -> str:
    return "Goodbye, World!"


#  ___________________
#  Import LIBRARIES
#  Import FILES
#  ___________________

# def main():
#     print("Hello from git-demo!")

# if __name__ == "__main__":
#     main()
