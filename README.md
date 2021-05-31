# Smart Health Prediction System
#### [소프트웨어 공학 1분반]
#### 0. 프로젝트명 : Smart Health Prediction System  
(사이트 : https://nevonprojects.com/smart-health-prediction-using-data-mining/)

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

- CAUnseling은 사용자 지원 및 온라인 상담 프로젝트로,  
사용자가 온라인상에서 의료 시스템을 통해 건강 문제에 대한 즉각적인 지침을 얻을 수 있는 시스템입니다.   


- 의사의 경우, 환자 세부 정보와 해당 환자의 보고서를 볼 수 있습니다.  
또한, 환자의 예측에 따라 환자가 무엇을 검색했는지에 대한 세부 정보를 보거나 환자의 개인 정보를 볼 수 있습니다.  


- 관리자는 데이터베이스에 질병의 유형과 증상을 지정하여 새로운 질병 세부 정보를 추가하고,  
데이터베이스에 저장된 다양한 질병 및 증상을 볼 수 있습니다.  
 


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
- [랜딩페이지](admin/06.%203rd%20checkpoint/00.%20home.png)
- [Admin](admin/06.%203rd%20checkpoint)  
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
