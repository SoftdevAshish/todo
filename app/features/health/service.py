from datetime import datetime, timezone
from typing import Dict, Any, Callable, Awaitable

from app.core.logger import get_logger
from app.dependencies.all_enum import HealthStatus

logger = get_logger()


class HealthService:

    def __init__(self):
        self._service: Dict[str, HealthStatus] = {}
        self._check_function: Callable[[], Awaitable[bool]] = {}
        self._timeout: Dict[str, float] = {}
        self._retry_delay: Dict[str, float] = {}
        self._max_retries: Dict[str, int] = {}
        self._dependencies: Dict[str, set[str]] = {}
        self._last_check: Dict[str, datetime] = {}

    async def validate_dependencies(self):
        pass

    async def check_health(self, service_name: str, depends_on: Dict[str, Any]) -> None:
        if not depends_on:
            return
        for dependency in depends_on:
            if dependency not in self._service:
                raise ValueError(f"Dependency {dependency} not registered for service {service_name}")

    async def add_service(self, service_name: str,
                          check_function: Callable[[], Awaitable[bool]],
                          timeout: float = 5.0,
                          retry_delay: float = 1.0,
                          max_retries: int = 3,
                          depends_on: list[str] | None = None,
                          ) -> None:

        self._service[service_name] = service_name
        self._check_function[check_function] = check_function
        self._timeout[service_name] = timeout
        self._retry_delay[service_name] = retry_delay
        self._max_retries[service_name] = max_retries
        self._last_check[service_name] = datetime.now(timezone.utc)
        if depends_on:
            await self.validate_dependencies(service_name, depends_on)
            self._dependencies[service_name] = set(depends_on)
            logger.info(f"Service {service_name} registered with depends on {depends_on}")


