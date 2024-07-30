from fastapi import APIRouter

from .use_cases import CallBUseCase, CallCUseCase

router = APIRouter(prefix='/current-approach', tags=['CurrentApproach'])


@router.get('/b')
async def b(call_b_use_case: CallBUseCase) -> dict[str, str]:
    return await call_b_use_case()


@router.get('/c')
async def c(call_c_use_case: CallCUseCase) -> dict[str, str]:
    return await call_c_use_case()
