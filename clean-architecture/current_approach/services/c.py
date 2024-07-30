from typing import Annotated, Protocol, Self

from fastapi import Depends

from .a import ServiceA, ServiceAProtocol


class ServiceCProtocol(Protocol):
    async def method(self: Self) -> dict[str, str]: ...


class ServiceCImpl:
    def __init__(self, service_a: ServiceAProtocol) -> None:
        self.service_a = service_a

    async def method(self: Self) -> dict[str, str]:
        return {'method3': await self.service_a.method3()}


async def get_service_c(service_a: ServiceA) -> ServiceCProtocol:
    return ServiceCImpl(service_a)


ServiceC = Annotated[ServiceCProtocol, Depends(get_service_c)]
