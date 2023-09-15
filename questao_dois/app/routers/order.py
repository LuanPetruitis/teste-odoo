from app.service.order import Order
from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/order", tags=["Pedidos"])


order_service = Order()


@router.get("/all")
def all_orders(user_id: str):
    orders = order_service.all_orders(user_id)
    if not orders:
        return JSONResponse(
            content=jsonable_encoder({"message": "Nenhum pedido foi encontrado!"}),
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return JSONResponse(
        content=jsonable_encoder(orders),
        status_code=status.HTTP_200_OK,
    )
