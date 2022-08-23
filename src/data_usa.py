from requests import get


class DataUSA:
	def __init__(self):
		self.api = "https://datausa.io/api"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}

	def get_data(
			self,
			drill_downs: str,
			measures: str,
			year: str = "latest"):
		return get(
			f"{self.api}/data?drilldowns={drill_downs}&measures={measures}&year={year}",
			headers=self.headers).json()
