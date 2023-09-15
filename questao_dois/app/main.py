from http import HTTPStatus

from app.routers import order, product, shopping_cart
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="E-commerce",
    description="Rotas para o seu E-commerce de sucesso!",
    contact={
        "name": "Luan Rodrigues Petruitis",
        "url": "https://www.linkedin.com/in/luanpetruitis/",
    },
)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(product.router)
app.include_router(shopping_cart.router)
app.include_router(order.router)


@app.get("/health_check", status_code=HTTPStatus.NO_CONTENT)
async def get_health_check():
    return Response(status_code=HTTPStatus.NO_CONTENT.value)
