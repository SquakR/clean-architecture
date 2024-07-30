from typing import Protocol, Self


class ServiceAProtocol(Protocol):
    async def method1(self: Self) -> str: ...

    async def method2(self: Self) -> str: ...


class ServiceB:
    def __init__(self, service_a: ServiceAProtocol) -> None:
        self.service_a = service_a

    async def method(self: Self) -> dict[str, str]:
        return {'method1': await self.service_a.method1(), 'method2': await self.service_a.method2()}
