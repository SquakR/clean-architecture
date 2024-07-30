from typing import Annotated

from fastapi import Depends

from .services import get_service_b, get_service_c
from ..use_cases import CallBUseCase, CallCUseCase
from ..use_cases.call_b import ServiceBProtocol
from ..use_cases.call_c import ServiceCProtocol


async def get_call_b_use_case(service_b: Annotated[ServiceBProtocol, Depends(get_service_b)]) -> CallBUseCase:
    return CallBUseCase(service_b)


async def get_call_c_use_case(service_c: Annotated[ServiceCProtocol, Depends(get_service_c)]) -> CallCUseCase:
    return CallCUseCase(service_c)
