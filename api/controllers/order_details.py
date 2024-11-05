from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import models, schemas


def create(db: Session, order_detail):
    db_order_detail = models.OrderDetail(
        order_id=order_detail.order_id,
        sandwich_id=order_detail.sandwich_id,
        amount=order_detail.amount,
    )
    db.add(db_order_detail)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail


def read_all(db: Session):
    return db.query(models.Order_detail).all()


def read_one(db: Session, order_detail_id):
    return db.query(models.Order_detail).filter(models.Order_detail.id == order_detail_id).first()


def update(db: Session, order_detail_id, order_detail):
    db_order_detail = db.query(models.Order_detail).filter(models.Order_detail.id == order_detail_id)
    update_data = order_detail.model_dump(exclude_unset=True)
    db_order_detail.update(update_data, synchronize_session=False)
    db.commit()
    return db_order_detail.first()


def delete(db: Session, order_detail_id):
    db_order_detail = db.query(models.Order_detail).filter(models.Order_detail.id == order_detail_id)
    db_order_detail.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)