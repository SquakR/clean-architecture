from typing import Annotated, Protocol, Self

from fastapi import Depends

from .a import ServiceA, ServiceAProtocol


class ServiceBProtocol(Protocol):
    async def method(self: Self) -> dict[str, str]: ...


class ServiceBImpl:
    def __init__(self, service_a: ServiceAProtocol) -> None:
        self.service_a = service_a

    async def method(self: Self) -> dict[str, str]:
        return {'method1': await self.service_a.method1(), 'method2': await self.service_a.method2()}


async def get_service_b(service_a: ServiceA) -> ServiceBProtocol:
    return ServiceBImpl(service_a)


ServiceB = Annotated[ServiceBProtocol, Depends(get_service_b)]
