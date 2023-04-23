from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from src.schemas import cook_step
from src.schemas.user import UserOut
from src.services import cook_steps
from src.services.user import user
from src.database.dependencies import get_async_session


router = APIRouter()

@router.get("/cook_steps")
async def get_cook_steps(session: Session = Depends(get_async_session)):
    return await cook_steps.get_cook_step(session)

@router.post("/add_cook_step")
async def add_step(step: cook_step.Cook_stepAdd, session: Session = Depends(get_async_session) ):
    return await cook_steps.create_cook_step(session=session, cook_step=step)

@router.patch("/cook_step/{id}")
async def update_step(id: int, step: cook_step.Cook_stepAdd, session: Session = Depends(get_async_session) ):
    return await cook_steps.update_cook_step(session=session, step=step, id=id)

@router.delete("/cook_step/{id}")
async def delete_step(id: int, session: Session = Depends(get_async_session) ):
    return await cook_steps.delete_cook_step(session=session, id=id)

@router.get("/time_cook/{time_from}/{time_to}")
async def get_time(time_from: int, time_to: int, session: Session = Depends(get_async_session) ):
    return await cook_steps.filter_cook_time(session=session, time_from=time_from, time_to=time_to)
