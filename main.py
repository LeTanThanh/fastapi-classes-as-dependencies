from fastapi import FastAPI
from fastapi import Depends

from typing import Annotated

app = FastAPI()

# Classes as dependencies

class CommonQueryParams:
  def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100) -> None:
    self.q = q
    self.skip = skip
    self.limit = limit

ITEMS = [
  {"item_name": "Foo"},
  {"item_name": "Bar"},
  {"item_name": "Baz"}
]

@app.get("/items")
async def read_items(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
  response = {}

  if commons.q:
    response.update({"q": q})

  start = commons.skip
  end = commons.skip + commons.limit
  items = ITEMS[start : end]
  response.update({"items": items})

  return response
