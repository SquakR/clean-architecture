from typing import Protocol, Self


class ServiceAProtocol(Protocol):
    async def method3(self: Self) -> str: ...


class ServiceC:
    def __init__(self, service_a: ServiceAProtocol) -> None:
        self.service_a = service_a

    async def method(self: Self) -> dict[str, str]:
        return {'method3': await self.service_a.method3()}
