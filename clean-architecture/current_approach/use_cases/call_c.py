from typing import Annotated, Protocol, Self

from fastapi import Depends

from ..services import ServiceC, ServiceCProtocol


class CallCUseCaseProtocol(Protocol):
    async def __call__(self: Self) -> dict[str, str]: ...


class CallCUseCaseImpl:
    def __init__(self, service_c: ServiceCProtocol) -> None:
        self.service_c = service_c

    async def __call__(self: Self) -> dict[str, str]:
        return await self.service_c.method()


async def get_call_c_use_case(service_c: ServiceC) -> CallCUseCaseProtocol:
    return CallCUseCaseImpl(service_c)


CallCUseCase = Annotated[CallCUseCaseProtocol, Depends(get_call_c_use_case)]
