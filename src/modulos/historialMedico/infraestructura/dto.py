from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.config.db import Base
import uuid
import os

def get_uuid():
    return str(uuid.uuid4())

def default_list():
    return []

class HistorialMedicoDTO(Base):    
    __tablename__ = "historial_medico"

    if os.getenv("FLASK_ENV") == "test":
        id = Column(String, primary_key=True, default=get_uuid)
        paciente_id = Column(String, ForeignKey("paciente.id", ondelete="SET NULL"), nullable=True)
        diagnostico_id = Column(String, ForeignKey("diagnostico.id", ondelete="SET NULL"), nullable=True)
    else:
        id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
        paciente_id = Column(UUID(as_uuid=True), ForeignKey("paciente.id", ondelete="SET NULL"), nullable=True)
        diagnostico_id = Column(UUID(as_uuid=True), ForeignKey("diagnostico.id", ondelete="SET NULL"), nullable=True)
    
    paciente = relationship("PacienteDTO", back_populates="historial_medico")
    diagnostico = relationship("DiagnosticoDTO", back_populates="historial_medico")

class PacienteDTO(Base):
    __tablename__ = "paciente"
    if os.getenv("FLASK_ENV") == "test":
        id = Column(String, primary_key=True, default=get_uuid)
    else:
        id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    token = Column(String, nullable=False)

    grupo_etario = Column(String, nullable=False)
    genero = Column(String, nullable=False)
    etnia = Column(String, nullable=False)
    historial_medico = relationship("HistorialMedicoDTO", back_populates="paciente")

class DiagnosticoDTO(Base):
    __tablename__ = "diagnostico"

    if os.getenv("FLASK_ENV") == "test":
        id = Column(String, primary_key=True, default=get_uuid)
    else:
        id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    descripcion = Column(String, nullable=False)
    entorno_clinico = Column(String, nullable=False)
    sintomas = Column(String, nullable=False)
    contexto_procesal = Column(String, nullable=False)
    historial_medico = relationship("HistorialMedicoDTO", back_populates="diagnostico")
    

    