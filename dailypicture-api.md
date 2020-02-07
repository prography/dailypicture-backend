# Daily Picture API

#### <사용자 등록, 토큰 발급 제외> 항상 공통으로 항상 넣어줘야 할 것‼️

#### request-header

| key           | value     | description   |
| ------------- | --------- | ------------- |
| Authorization | Token 123 | 123은 토큰 값 |

```
Autorization: Token 123
```

형태로 헤더에 토큰을 넣어줘야 함



## 사용자 등록

~~~url
post /accounts/
~~~

##### request-body

| name | type   | description               |
| ---- | ------ | ------------------------- |
| uuid | string | 안드로이드 기기의 uuid 값 |

##### response-body

| name | type   | description               |
| ---- | ------ | ------------------------- |
| uuid | string | 안드로이드 기기의 uuid 값 |



## 토큰 발급

~~~url
post /api-token-auth/
~~~

##### request-body

| name     | type   | description                      |
| -------- | ------ | -------------------------------- |
| username | string | 안드로이드 기기의 uuid 값과 동일 |
| password | string | 안드로이드 기기의 uuid 값과 동일 |

##### response-body

| name  | type   | description |
| ----- | ------ | ----------- |
| token | string | 토큰 값     |



## 목표 리스트

~~~url
GET /posts/
~~~

##### response-body

| name      | type    | description        |
| --------- | ------- | ------------------ |
| id        | integer | post 의 id 값      |
| user_id   | string  | username (uuid 값) |
| title     | string  | 목표 제목          |
| thumbnail | string  | 목표 대문 사진     |
| status    | boolean | 완료 상태          |



## 목표 등록하기

~~~url
POST /posts/
~~~

##### url-parameter

| name    | type    | description |
| ------- | ------- | ----------- |
| post_id | integer | post의 id값 |

##### request-body

| name      | type   | description       |
| --------- | ------ | ----------------- |
| title     | string | 목표 제목         |
| thumbnail | file   | 이미지(png, jpeg) |

##### response-body

| name       | type    | description    |
| ---------- | ------- | -------------- |
| id         | integer | post 의 id 값  |
| owner      | string  | 유저 이름      |
| title      | string  | 목표 제목      |
| thumbnail  | string  | 목표 대문 사진 |
| status     | boolean | 완료 상태      |
| created_at | string  | 생성 날짜      |
| days_count | int     | 디데이+        |



## 목표 상세보기

~~~url
POST /posts/{post_id}
~~~

##### url-parameter

| name    | type    | description |
| ------- | ------- | ----------- |
| post_id | integer | post의 id값 |

##### response-body

| name       | type    | description            |
| ---------- | ------- | ---------------------- |
| id         | integer | post 의 id 값          |
| owner      | string  | 유저 이름              |
| created_at | string  | 만든 날짜              |
| title      | string  | 목표 제목              |
| status     | boolean | 완료 상태              |
| images     | list    | 목표에 등록된 이미지들 |



## 목표 삭제하기

~~~url
DELETE /posts/{post_id}
~~~

##### url-parameter

| name    | type    | description                     |
| ------- | ------- | ------------------------------- |
| post_id | integer | post id의 숫자 값을 넣어줘야 함 |



## 사진 등록하기

~~~url
POST /images/create
~~~

##### request-body

| key  | value | description |
| ---- | ----- | ----------- |
| post | int   | post id 값  |
| url  | file  | 이미지 파일 |

##### response-body

| name       | type    | description    |
| ---------- | ------- | -------------- |
| id         | integer | image 의 id 값 |
| url        | string  | 이미지 링크    |
| days_count | integer | 디데이 +       |



## 사진 상세보기

~~~url
POST /images/{image_id}
~~~

##### url-parameter

| name     | type    | description                      |
| -------- | ------- | -------------------------------- |
| image_id | integer | image id의 숫자 값을 넣어줘야 함 |

##### response-body

| name       | type    | description    |
| ---------- | ------- | -------------- |
| id         | integer | image 의 id 값 |
| url        | string  | 이미지 링크    |
| days_count | integer | 디데이 +       |



## 사진 삭제하기

~~~url
DELETE /images/{image_id}
~~~

##### url-parameter

| name     | type    | description                      |
| -------- | ------- | -------------------------------- |
| image_id | integer | image id의 숫자 값을 넣어줘야 함 |



## 동영상 내보내기

~~~url
POST /videos/{post_id}/video
~~~

##### url-parameter

| name    | type    | description                     |
| ------- | ------- | ------------------------------- |
| post_id | integer | post id의 숫자 값을 넣어줘야 함 |

##### response-body

| name      | type   | description |
| --------- | ------ | ----------- |
| video_url | string | 비디오 링크 |

