from typing import Self


class ServiceA:
    async def method1(self: Self) -> str:
        return f'{self.__class__.__name__}, {self.method1.__name__}'

    async def method2(self: Self) -> str:
        return f'{self.__class__.__name__}, {self.method2.__name__}'

    async def method3(self: Self) -> str:
        return f'{self.__class__.__name__}, {self.method3.__name__}'
