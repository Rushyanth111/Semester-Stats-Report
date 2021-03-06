from semester_stats_report.reciepts import DepartmentReciept
from semester_stats_report.reports import DepartmentReport

from .httpclient import BaseClient


class DeptClient(BaseClient):
    def __init__(self, url: str, dept: str) -> None:
        """Client WRT to /dept/ Route

        Args:
            url (str): Url of the Server
            dept (str): Department Required.
        """
        super().__init__(url + "/dept")
        self.dept = dept

    async def get(self) -> DepartmentReport:
        """Get the Department

        Returns:
            DepartmentReport: Deparment Report with Details.
        """
        res = await self._get("/{}".format(self.dept))
        rec = DepartmentReciept.parse_obj(res)
        return rec

    async def update(self, report: DepartmentReport):
        """Update a Department

        Args:
            report (DepartmentReport): Department Report
        """
        res = await self._put("/{}".format(self.dept), body=report.dict())
        return res

    async def add(self, report: DepartmentReport):
        """Send a Department

        Args:
            report (DepartmentReport): Department Report
        """
        res = await self._post("/", body=report.dict())
        return res
