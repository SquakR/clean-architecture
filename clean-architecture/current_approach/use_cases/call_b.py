from typing import Annotated, Protocol, Self

from fastapi import Depends

from ..services import ServiceB, ServiceBProtocol


class CallBUseCaseProtocol(Protocol):
    async def __call__(self: Self) -> dict[str, str]: ...


class CallBUseCaseImpl:
    def __init__(self, service_b: ServiceBProtocol) -> None:
        self.service_b = service_b

    async def __call__(self: Self) -> dict[str, str]:
        return await self.service_b.method()


async def get_call_b_use_case(service_b: ServiceB) -> CallBUseCaseProtocol:
    return CallBUseCaseImpl(service_b)


CallBUseCase = Annotated[CallBUseCaseProtocol, Depends(get_call_b_use_case)]
