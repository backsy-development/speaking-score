from dotenv import load_dotenv
import os

load_dotenv()

class AppConfig:
  port = 4102

  def __init__(self):
    self.port = os.getenv("PORT") if os.getenv("PORT") else self.port