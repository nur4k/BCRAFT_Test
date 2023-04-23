from fastapi import HTTPException, Query

from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

from src.schemas import cook_step
from src.database.models.models import Cook_Step


async def get_cook_step(session: Session):
    return (await session.scalars(select(Cook_Step))).all()

async def create_cook_step(session: Session, cook_step: cook_step.Cook_stepAdd):
    query = Cook_Step(**cook_step.dict())
    session.add(query)
    await session.commit()
    return query

async def update_cook_step(session: Session, id: int, step: cook_step.Cook_stepAdd):
    cook_step = await session.scalar(select(Cook_Step).where(Cook_Step.id == id))
    if not cook_step:
        raise HTTPException("Error!!!")
    elif step.step:
        await session.execute(update(Cook_Step).where(Cook_Step.id == id).values(step=step.step))
        await session.commit()
    elif step.time:
        await session.execute(update(Cook_Step).where(Cook_Step.id == id).values(time=step.time))
        await session.commit()
    elif step.description:
        await session.execute(update(Cook_Step).where(Cook_Step.id == id).values(description=step.description))
        await session.commit()
    elif step.recipe:
        await session.execute(update(Cook_Step).where(Cook_Step.id == id).values(recipe=step.recipe))
        await session.commit()
    return {"msg":"Succesfull update cook_step!"}

async def delete_cook_step(session: Session, id: int):
    cook_step = await session.scalar(select(Cook_Step).where(Cook_Step.id == id))
    if not cook_step:
        raise HTTPException("Error!!!")
    await session.execute(delete(Cook_Step).where(Cook_Step.id == id))
    await session.commit()
    return {"msg": "Post deleted!"}

async def filter_cook_time(session: Session, time_from : int = Query(None, gt=0), time_to: int = Query(None, gt=0)):
    cook_steps = (await session.scalars(select(Cook_Step).where(Cook_Step.time >= time_from, Cook_Step.time <= time_to))).all()
    if not cook_steps:
        return {"msg": "Time is not found!"}
    return cook_steps
