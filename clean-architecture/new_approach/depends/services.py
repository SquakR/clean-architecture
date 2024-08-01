from typing import Annotated

from fastapi import Depends

from ..services import ServiceA, ServiceB, ServiceC
from ..services.b import ServiceAProtocol as BServiceAProtocol
from ..services.c import ServiceAProtocol as CServiceAProtocol


async def get_service_a() -> ServiceA:
    return ServiceA()


async def get_service_b(service_a: Annotated[BServiceAProtocol, Depends(get_service_a)]) -> ServiceB:
    return ServiceB(service_a)


async def get_service_c(service_a: Annotated[CServiceAProtocol, Depends(get_service_a)]) -> ServiceC:
    return ServiceC(service_a)
