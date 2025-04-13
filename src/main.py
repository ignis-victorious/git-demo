#  ___________________
#  Import LIBRARIES
from fastapi import FastAPI
#  Import FILES
#  ___________________


app: FastAPI = FastAPI()


@app.get("/")
def hello(name: str = "World") -> str:
    return f"Hello, {name}!"


#  ___________________
#  Import LIBRARIES
#  Import FILES
#  ___________________

# def main():
#     print("Hello from git-demo!")

# if __name__ == "__main__":
#     main()
