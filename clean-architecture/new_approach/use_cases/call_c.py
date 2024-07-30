from typing import Protocol, Self


class ServiceCProtocol(Protocol):
    async def method(self: Self) -> dict[str, str]: ...


class CallCUseCase:
    def __init__(self, service_c: ServiceCProtocol) -> None:
        self.service_c = service_c

    async def __call__(self: Self) -> dict[str, str]:
        return await self.service_c.method()
