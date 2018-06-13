import requests
from bs4 import BeautifulSoup as bs
from tools.json_mounter import JsonMounter


class SidoYehwe:
    def __init__(self):
        self.content_url = "http://info.nec.go.kr/electioninfo/electionInfo_report.xhtml"
        self.city_url = "http://info.nec.go.kr/bizcommon/selectbox/selectbox_cityCodeBySgJson.json"
        self.gsg_url = "http://info.nec.go.kr/bizcommon/selectbox/selectbox_townCodeJson.json"
        self.sgg_url = "http://info.nec.go.kr/bizcommon/selectbox/selectbox_getSggTownCodeJson.json"

    def _fetch_content(self, *args, **kwargs):
        kwargs = {
            "electionId": kwargs.get("electionId", "0020180613"),
            "requestURI": kwargs.get("requestURI", "/WEB-INF/jsp/electioninfo/0020180613/cp/cpri03.jsp"),
            "topMenuId": kwargs.get("topMenuId", "CP"),
            "secondMenuId": kwargs.get("secondMenuId", "CPRI03"),
            "menuId": kwargs.get("menuId", "CPRI03"),
            "statementId": kwargs.get("statementId", "CPRI03_#5"),
            "electionCode": kwargs.get("electionCode", 5),
            "cityCode": kwargs.get("cityCode", 1100),
            "townCode": kwargs.get("townCode", 1101),
            "sggTownCode": kwargs.get("sggTownCode", 5110101),
            "propotionalRepresentationCode": kwargs.get("propotionalRepresentationCode", -1),
            "dateCode": kwargs.get("dateCode", 0),
            "x": kwargs.get("x", 14),
            "y": kwargs.get("y", 14)
        }

        resp = requests.post(self.content_url, data=kwargs)
        return resp

    def _parse_content(self, resp: requests.Response, *args, **kwargs):
        interested = kwargs.get("interested", [1, 3, 7, 9, 11, 13])
        if resp.status_code != 200:
            raise Exception("Connection has not been successfully ended")

        soup = bs(resp.text, 'html.parser')
        candidates = soup.select("table#table01 > tbody > tr")

        result = []
        for cand in candidates:
            result.append([cand.contents[k] for k in interested])

        return result

    def _fetch_city_code(self, *args, **kwargs):
        electionId = kwargs.get("electionId", "0020180613")
        electionCode = kwargs.get("electionCode", 5)

        resp = requests.post(self.city_url, data={"electionId": electionId, "electionCode": electionCode})
        return resp

    def _get_city_codes(self, *args, **kwargs):
        resp = self._fetch_city_code(*args, **kwargs)

        data = JsonMounter(resp.json())

        return [(v.CODE, v.NAME) for v in data.jsonResult.body]

    def _fetch_gsg_code(self, *args, **kwargs):
        kwargs = {
            "electionId": kwargs.get("electionId", "0020180613"),
            "electionCode": kwargs.get("electionCode", 5),
            "cityCode": kwargs.get("cityCode", 1100)
        }

        resp = requests.post(self.gsg_url, data=kwargs)
        return resp

    def _get_gsg_codes(self, *args, **kwargs):
        resp = self._fetch_gsg_code(*args, **kwargs)

        data = JsonMounter(resp.json())

        return [(v.CODE, v.NAME) for v in data.jsonResult.body]

    def _fetch_sgg_code(self, *args, **kwargs):
        kwargs = {
            "electionId": kwargs.get("electionId", "0020180613"),
            "electionCode": kwargs.get("electionCode", 5),
            "townCode": kwargs.get("townCode", 1101)
        }

        resp = requests.post(self.sgg_url, data=kwargs)
        return resp

    def _get_sgg_codes(self, *args, **kwargs):
        resp = self._fetch_sgg_code(*args, **kwargs)

        data = JsonMounter(resp.json())

        return [(v.CODE, v.NAME) for v in data.jsonResult.body]

    def parse(self):
        codes = self._get_city_codes()

        total = {}
        for code, name in codes:
            total[code] = {}
            for town, town_name in self._get_gsg_codes(cityCode=code):
                total[code][town] = {}
                for sgg, sgg_name in self._get_sgg_codes(townCode=town):
                    total[code][town][sgg] = []
                    candidates = self._parse_content(self._fetch_content(cityCode=code, townCode=town, sggTownCode=sgg), interested=[1, 3, 7, 9, 11, 13])

                    for cand in candidates:
                        temp = []
                        for idx in range(len(cand)):
                            if idx == 1:
                                temp.append(cand[idx].contents[1]['src'])
                            elif idx == 3:
                                _name = cand[idx].contents[1]
                                _a = _name.contents[0]
                                temp.append(cand[idx].contents[1].contents[0].strip())
                            else:
                                temp.append(cand[idx].text)

                        total[code][town][sgg].append(temp)

        return total