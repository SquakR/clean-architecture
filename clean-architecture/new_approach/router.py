from typing import Annotated, Protocol, TypeVar

from fastapi import APIRouter, Depends

from .di.use_cases import get_call_b_use_case, get_call_c_use_case

UseCaseResultSchemaType = TypeVar('UseCaseResultSchemaType', covariant=True)


class UseCaseProtocol(Protocol[UseCaseResultSchemaType]):
    async def __call__(self) -> UseCaseResultSchemaType: ...


router = APIRouter(prefix='/new-approach', tags=['NewApproach'])


@router.get('/b')
async def b(
    call_b_use_case: Annotated[UseCaseProtocol[dict[str, str]], Depends(get_call_b_use_case)]
) -> dict[str, str]:
    return await call_b_use_case()


@router.get('/c')
async def c(
    call_b_use_case: Annotated[UseCaseProtocol[dict[str, str]], Depends(get_call_c_use_case)]
) -> dict[str, str]:
    return await call_b_use_case()
