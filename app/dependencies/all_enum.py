from enum import Enum

class Environment(str, Enum):
    DEV = "dev"
    PROD = "prod"

class HealthStatus(str, Enum):
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    DEGRADED = "degraded"
    STARTING = "starting"
    DOWN = "down"
