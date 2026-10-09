
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user
from app.models import Habit, User
from app.schemas import HabitCreate, HabitResponse, HabitUpdate


router = APIRouter(
    prefix="/habits",
    tags=["Habits"]
)


@router.post(
    "/",
    response_model=HabitResponse,
    status_code=status.HTTP_201_CREATED
)
def create_habit(
    habit_data: HabitCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    habit = Habit(
        **habit_data.model_dump(),
        owner_id=current_user.id
    )

    db.add(habit)
    db.commit()
    db.refresh(habit)

    return habit


@router.get("/", response_model=list[HabitResponse])
def get_habits(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return (
        db.query(Habit)
        .filter(Habit.owner_id == current_user.id)
        .all()
    )


@router.get("/{habit_id}", response_model=HabitResponse)
def get_habit(
    habit_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    habit = (
        db.query(Habit)
        .filter(
            Habit.id == habit_id,
            Habit.owner_id == current_user.id
        )
        .first()
    )

    if habit is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Habit not found"
        )

    return habit


@router.put("/{habit_id}", response_model=HabitResponse)
def update_habit(
    habit_id: int,
    habit_data: HabitUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    habit = (
        db.query(Habit)
        .filter(
            Habit.id == habit_id,
            Habit.owner_id == current_user.id
        )
        .first()
    )

    if habit is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Habit not found"
        )

    update_data = habit_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(habit, field, value)

    db.commit()
    db.refresh(habit)

    return habit


@router.delete("/{habit_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_habit(
    habit_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    habit = (
        db.query(Habit)
        .filter(
            Habit.id == habit_id,
            Habit.owner_id == current_user.id
        )
        .first()
    )

    if habit is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Habit not found"
        )

    db.delete(habit)
    db.commit()

    return None
