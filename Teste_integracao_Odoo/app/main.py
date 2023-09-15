from fastapi import Body, FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Integração de Faturas",
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


@app.post("/")
def invoices(data: dict = Body(...)):
    if not data:
        return JSONResponse(
            content=jsonable_encoder({
                "message": "Payload está vazio.",
                "data": data
            }),
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return JSONResponse(
        content=jsonable_encoder({
            "message": "Fatura criada com sucesso.",
            "data": data,
            "id": "11111"
        }),
        status_code=status.HTTP_200_OK,
    )
