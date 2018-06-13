## 시도지사선거
### Parse Trace
```markdown
시도
선거구명, 사진, 소속정당명, 성명, 성별, 생년월일
````

### URIs
```markdown
[ 메인 ]
POST http://info.nec.go.kr/electioninfo/electionInfo_report.xhtml
PayL
    electionId	            0020180613
    requestURI	            /WEB-INF/jsp/electioninfo/0020180613/cp/cpri03.jsp
    topMenuId	            CP
    secondMenuId            CPRI03
    menuId                  CPRI03
    statementId             CPRI03_#3
    electionCode            3
    cityCode                1100
    proportionalRepresentationCode	-1
    townCode	            -1
    dateCode	            0
    x       	            14
    y	                    14

[ 시도 ]
POST http://info.nec.go.kr/bizcommon/selectbox/selectbox_cityCodeBySgJson.json
PayL
    electionId      0020180613
    electionCode    3
```



## 구시군의장선거
### Parse Trace
```markdown
시도
선거구
선거구명, 사진, 소속정당명, 성명, 성별, 생년월일
```

### URIs
```markdown
[ 메인 ]
POST http://info.nec.go.kr/electioninfo/electionInfo_report.xhtml
PayL
    electionId              0020180613
    requestURI              /WEB-INF/jsp/electioninfo/0020180613/cp/cpri03.jsp
    topMenuId               CP
    secondMenuId            CPRI03
    menuId                  CPRI03
    statementId             CPRI03_#4
    electionCode            4
    cityCode                1100
    sggCityCode             4110100
    proportionalRepresentationCode	-1
    townCode                -1
    dateCode                0
    x                       48
    y                       9

[ 시도 ]
POST http://info.nec.go.kr/bizcommon/selectbox/selectbox_cityCodeBySgJson.json
PayL
    electionId      0020180613
    electionCode    4

[ 선거구 ]
POST http://info.nec.go.kr /bizcommon/selectbox/selectbox_getSggCityCodeJson.json
PayL
    electionId      0020180613
    electionCode    4
    cityCode        1100
```



## 시도의회의원선거
### Parse Trace
```markdown
시도
구시군
선거구(구시군)
선거구명, 사진, 소속정당명, 성명, 성별, 생년월일
```

### URIs
```markdown
[ 메인 ]
POST http://info.nec.go.kr/electioninfo/electionInfo_report.xhtml
PayL
    electionId              0020180613
    requestURI              /WEB-INF/jsp/electioninfo/0020180613/cp/cpri03.jsp
    topMenuId               CP
    secondMenuId            CPRI03
    menuId                  CPRI03
    statementId             CPRI03_#5
    electionCode            5
    cityCode                1100
    townCode                1101
    sggTownCode             5110101
    proportionalRepresentationCode	-1
    dateCode                0
    x                       19
    y                       8

[ 시도 ]
POST http://info.nec.go.kr/bizcommon/selectbox/selectbox_cityCodeBySgJson.json
PayL
    electionId      0020180613
    electionCode    5

[ 구시군 ]
POST http://info.nec.go.kr/bizcommon/selectbox/selectbox_cityCodeBySgJson.json
PayL
    electionId      0020180613
    electionCode    5

[ 선거구 ]
POST http://info.nec.go.kr /bizcommon/selectbox/selectbox_getSggCityCodeJson.json
PayL
    electionId      0020180613
    electionCode    5
    townCode        1101
```



## 구시군의회의원선거
### Parse Trace
```markdown
시도
구시군
선거구(구시군)
선거구명, 사진, 소속정당명, 성명, 성별, 생년월일
```