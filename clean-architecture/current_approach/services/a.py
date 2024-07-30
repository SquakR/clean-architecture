from typing import Annotated, Protocol, Self

from fastapi import Depends


class ServiceAProtocol(Protocol):
    async def method1(self: Self) -> str: ...

    async def method2(self: Self) -> str: ...

    async def method3(self: Self) -> str: ...


class ServiceAImpl:
    async def method1(self: Self) -> str:
        return f'{self.__class__.__name__}, {self.method1.__name__}'

    async def method2(self: Self) -> str:
        return f'{self.__class__.__name__}, {self.method2.__name__}'

    async def method3(self: Self) -> str:
        return f'{self.__class__.__name__}, {self.method3.__name__}'


async def get_service_a() -> ServiceAProtocol:
    return ServiceAImpl()


ServiceA = Annotated[ServiceAProtocol, Depends(get_service_a)]
