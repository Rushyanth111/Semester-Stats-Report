from typing import List

from semester_stats_report.reports import (
    DepartmentReport,
    ScoreReport,
    StudentReport,
    SubjectReport,
)

from .httpclient import BaseClient


class BulkClient(BaseClient):
    def __init__(self, url: str) -> None:
        """Client WRT to /bulk

        Args:
            url (str): Url For the Endpoint
        """
        super().__init__(url + "/bulk")

    async def scores(self, reports: List[ScoreReport]):
        """/scores Endpoint

        Args:
            reports (List[ScoreReport]): List of Student Reports
        """
        return await self._post("/score", body=[x.dict() for x in reports])

    async def dept(self, reports: List[DepartmentReport]):
        """/dept Endpoint

        Args:
            reports (List[DepartmentReport]): List of Department Reports
        """
        return await self._post("/dept", body=[x.dict() for x in reports])

    async def subject(self, reports: List[SubjectReport]):
        """/subject Endpoint

        Args:
            reports (List[SubjectReport]): List of Subject Reports
        """
        return await self._post("/subject", body=[x.dict() for x in reports])

    async def student(self, reports: List[StudentReport]):
        """/student Endpoint

        Args:
            reports (List[StudentReport]): List of Student Reports.
        """
        return await self._post("/student", body=[x.dict() for x in reports])
