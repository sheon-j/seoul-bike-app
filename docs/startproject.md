# 프로젝트 생성

1. 폴더를 생성합니다.

   ```sh
   mkdir my_proj
   cd my_proj

   # Django Backend
   mkdir backend
   cd backend

   python -m venv .env
   source .env/bin/activate

   pip install Django djangorestframework django-cors-headers
   django-admin startproject config .
   python manage.py runserver

   # Nuxt Frontend
   cd ~/my_proj
   yarn create nuxt-app frontend
   cd frontend
   yarn dev
   ```

2. 추가 코드

   ```python
   # config.settings
   INSTALLED_APPS += ["rest_framework", "corsheaders"]
   CORS_ORIGIN_ALLOW_ALL = True
   MIDDLEWARE += [
       ...,
       "corsheaders.middleware.CorsMiddleware",
       "django.middleware.common.CommonMiddleware",
       ...
   ]
   ```

3. 샘플 코드

   ```js
   <script>
   export default {
     data() {
       return {
         message: "",
       }
     },

     async fetch() {
       const response = await fetch("http://localhost:8000/hello/")
       const jsonData = await response.json()
       this.message = jsonData.message
     },
   }
   </script>
   ```

4. 이슈

   - frontend 패키지 이슈 => yarn.lock 파일 대체
