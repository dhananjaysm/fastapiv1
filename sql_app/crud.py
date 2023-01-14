from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, status

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_master_row(db:Session , row_id:int):
    return db.query(models.MasterMains).filter(models.MasterMains.id == row_id).first()

def create_master_row(db:Session,master: schemas.Master):
    db_row = models.MasterMains(**master.dict())
    db.add(db_row)
    db.commit()
    db.refresh(db_row)
    return db_row

def create_log(db:Session, log:schemas.LoggerCreate, row_id:int):
    isMaster = get_master_row(db=db,row_id= row_id)
    if isMaster is None:
        raise HTTPException(status_code=404, detail="Row not found")
    db_log = models.Logger(**log.dict(),row_id= row_id)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log
    