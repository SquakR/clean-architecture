from typing import Protocol, Self


class ServiceBProtocol(Protocol):
    async def method(self: Self) -> dict[str, str]: ...


class CallBUseCase:
    def __init__(self, service_b: ServiceBProtocol) -> None:
        self.service_b = service_b

    async def __call__(self: Self) -> dict[str, str]:
        return await self.service_b.method()
