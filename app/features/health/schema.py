from pydantic import BaseModel

from app.dependencies.all_enum import HealthStatus


class ComponentHealth(BaseModel):
    status: HealthStatus
    error: str | None = None

class LivenessOut(BaseModel):
    status: HealthStatus

class HealthOut(BaseModel):
    status: HealthStatus
    check:dict[str, ComponentHealth]