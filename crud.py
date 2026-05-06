from db import SessionLocal
from models import Face

def insert_face(name, encoding):
    session = SessionLocal()

    face = Face(
        name=name,
        encoding=encoding
    )

    session.add(face)
    session.commit()
    session.close()
    
def find_closest_face(query_vector):
    session = SessionLocal()

    result = session.query(Face).order_by(
        Face.encoding.l2_distance(query_vector)
    ).first()

    session.close()

    return result

# 📋 Get all stored faces
def get_all_faces():
    session = SessionLocal()

    data = session.query(Face).all()

    session.close()
    return data