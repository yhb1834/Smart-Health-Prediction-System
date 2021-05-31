# CAUnseling
#### [소프트웨어 공학 1분반]
#### 0. 프로젝트명 : CAUnseling
(참고 사이트 : https://nevonprojects.com/smart-health-prediction-using-data-mining/)

#### 1. 팀원

|이름|학번|그룹 구분|역할|
|---|---|:---:|:---:|
|김효진|20181940|Admin|프론트엔드|
|배소현|20190539|Admin|백엔드|
|신동준|20191635|Patient|백엔드|
|이상진|20162191|Patient|프론트엔드|
|이한별|20195732|Doctor|프론트엔드|
|홍주표|20195520|Doctor|백엔드|


#### 2. 프로젝트 소개

- CAUnseling은 온라인 의사-환자 managing system으로,   
의사와 환자 모두가 만족할 수 있는 간편한 의사 예약 시스템입니다.


- 의사의 경우, 환자 예약목록, 처방전, 예약사항, 진료비 관리를 할 수 있습니다.  
또한, feedback 페이지에서 관리자나 진상환자에 대한 피드백이 가능합니다.


- 환자의 경우, 의사를 검색하고 진료 신청을 할 수 있으며, 진료 후에는 report를 확인할 수 있습니다.  
또한, details 페이지에서 환자 본인의 정보를 확인할 수 있으며, feedback 페이지를 통해 의사나 관리자에 대한 피드백이 가능합니다.


- 관리자는 의사 승인, 피드백 관리 등의 역할을 수행합니다. 
 


#### 3. 파트 분배 : admin login, patient login, doctor login
```
0) 공통 : home, main, signup, login, logout -> admin 팀이 대부분 작업함  
1) patient : search, searchlist, application, report, details, feedback  
2) doctor : patient-list, prescription, reservation, earnings, feedback  
3) admin : doctorcertify, feedback  
```


#### 4. The 1st Checkpoint
##### 1) Problem Statement
- [Problem Statement](./ProblemStatement.docx)
##### 2) User Story  
- [Admin](admin/01.%20User%20Story/UserStory.md)  
- [Doctor](doctor/UserStory/UserStory.md)  
- [Patient](patient/01.userstory/userstory.md) 
##### 3) Use Case model
- [Admin](admin/02.%20Use%20Case%20%26%20Domain%20Model)  
- [Doctor](doctor/Domain%20model/UseCase-Doctor.docx)  
- [Patient](patient/02.domainmodel/patient-Domain_model.docx)  
##### 4) UC Diagram
- [UC Diagram](./UC-Diagram.JPG)
##### 5) Domain model
- [Admin](admin/03.%20Domain%20Model%20Diagram)  
- [Doctor](doctor/Domain%20model)  
- [Patient](patient/02.domainmodel)  
##### 5) User Interface mockup  
- [User Interface mockup](./)  


#### 5. The 2nd Checkpoint
##### 1) Sequence Diagram
- [Admin](admin/04.%20Sequence%20Diagram)  
- [Doctor](doctor/System%20Sequence%20Diagram)  
- [Patient](patient/04.sequencediagram) 
##### 2) Class Diagram
- [Admin](admin/05.%20Class%20Diagram)  
- [Doctor](doctor/class%20diagram)  
- [Patient](patient/05.classdiagram)  
 

#### 6. The 3rd Checkpoint
- Before you check 3rd checkpoint, please read 장고 환경 세팅 방법.docx
- [랜딩페이지](admin/06.%203rd%20checkpoint/00.%20home.png)
- [Admin](admin/06.%203rd%20checkpoint/admin_3rd.md)  
- [Doctor](doctor/06.%203rd%20checkpoint)  
- [Patient](patient/06.%203rd%20checkpoint)  
  
  
#### 7. Meeting log
- [2021/04/12](meeting%20log/210412.md)
- [2021/04/16](meeting%20log/210416.md)
- [2021/04/17](meeting%20log/210417.md)
- [2021/04/23](meeting%20log/210423.md)
- [2021/05/06](meeting%20log/210506.md)
- [2021/05/11](meeting%20log/210511.md)
- [2021/05/14](meeting%20log/210514.md)
- [2021/05/18](meeting%20log/210518.md)
- [2021/05/22](meeting%20log/210522.md)
- [2021/05/26](meeting%20log/210526.md)
- [2021/05/29](meeting%20log/210529.md)
