"""
Django settings for tessco_blog project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from os import getenv, path
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('TESSCOBLOG_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

# google allauth setup line 39
SITE_ID=1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'app_user',
    'user_profile',
    'role',
    'category',
    'user_account',
    'article',
    'image',
    'user_follower',
    'article_like',
    'article_comment',
    # google allauth setup from line 56 - 57
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    # add tinymce
    'tinymce',
]

# google allauth setup from line 64 - 73
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email'
        ],
        'AUTH_PARAMS': {'access_type': 'online'}
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    #"django.contrib.auth.hashers.PBKDF2PasswordHasher",
]

ROOT_URLCONF = 'tessco_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(BASE_DIR /'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tessco_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': getenv('DB_ENGINE'),
        'NAME': getenv('DB_NAME'),
        'USER': getenv('DB_USER'),
        'PASSWORD': getenv('DB_PASSWORD'),
        'HOST': getenv('DB_HOST'),
        'PORT': 3306
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
# STATICFILES_DIR = path.join(BASE_DIR, 'static')
STATIC_ROOT = path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'app_user.User'

MEDIA_URL = 'media/'
MEDIA_ROOT = path.join(BASE_DIR, 'media')

# CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000'
]

# google allauth setup
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)

# django-allauth settings
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
# ACCOUNT_USERNAME_BLACKLIST = []
# ACCOUNT_SESSION_REMEMBER = None
# ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
# ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_UNIQUE_EMAIL = True
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_EMAIL_REQUIRED = True

# signs in users that logged using django-allauth without showing the google warning page.
SOCIALACCOUNT_LOGIN_ON_GET = True

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_ADAPTER = 'app_user.adapters.CustomAccountAdapter'

# ACCOUNT_FORMS = {
#     #'signup': 'app_user.forms.UserModelForm',
#     'login': 'app_user.forms.UserModelForm',
# }

#SESSION_COOKIE_SECURE = True
#SESSION_COOKIE_AGE = 1209600


# tinymce settings
# anchor pagebreak media code
# toolbar1: underline strikethrough fontsizeselect
# if (meta.filetype == "media") {
        # input.setAttribute("accept", "video/*");
    # }

TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'height': '400',
    'theme': 'silver',
    'plugins': '''
            save link image preview
            lists fullscreen insertdatetime nonbreaking
            directionality searchreplace wordcount visualblocks
            visualchars autolink charmap hr codesample
            ''',
    'toolbar1': '''
            undo redo | fullscreen preview bold italic | link image | alignleft alignright |
            aligncenter alignjustify | bullist numlist | fontsizeinput | codesample
            ''',
    # 'toolbar2': '''
    #         visualblocks visualchars |
    #         charmap hr pagebreak nonbreaking anchor |  code |
    #         ''',
    'contextmenu': 'formats | link image',
    'menubar': False,
    'statusbar': True,

    # 'images_upload_url': 'api/images',
    #'images_reuse_filename': True,
    # 'automatic_uploads': False, #
    'block_unsupported_drop': True,
    'file_picker_types': 'image',
    'images_file_types': 'jpeg, jpg, png, webp, jpe, jfi, jif, jfif',
    'images_upload_credentials': True,
    'image_caption': True,
    'image_dimensions': False,

    # manual codesample configuration
    # 'codesample_global_prismjs': True,
    # 'codesample_content_css': 'http://localhost:8000/article/static/article/css/prism.css',

    # 'forced_root_block': 'p',
    # 'newline_behavior': '',
    # 'newline_behavior': 'linebreak',
    # 'remove_trailing_brs': False,

    # Without this, the local image upload tab will not show
    # "file_picker_callback": '''
    #     function (cb, value, meta) {
    #         var input = document.createElement("input");
    #         input.setAttribute("type", "file");
    #         if (meta.filetype == "image") {
    #             input.setAttribute("accept", "image/*");
    #         }
    #         input.onchange = function () {
    #             var file = this.files[0];
    #             var reader = new FileReader();
    #             reader.onload = function () {
    #                 var id = "blobid" + (new Date()).getTime();
    #                 var blobCache = tinymce.activeEditor.editorUpload.blobCache;
    #                 var base64 = reader.result.split(",")[1];
    #                 var blobInfo = blobCache.create(id, file, base64);
    #                 blobCache.add(blobInfo);
    #                 cb(blobInfo.blobUri(), { title: file.name });
    #             };
    #         reader.readAsDataURL(file);
    #         };
    #     input.click();
    #     }
    # ''',

    # imgage_upload_handler is a javascript function to handle the upload
    'images_upload_handler': '''
        function example_image_upload_handler (blobInfo, success, failure, progress) {
            var xhr, formData;

            const form = document.querySelector('form');
            const articleFormData = new FormData(form);

            xhr = new XMLHttpRequest();
            xhr.withCredentials = true;
            xhr.open('POST', `${window.location.origin}/api/images`);

            xhr.setRequestHeader('X-CSRFToken', articleFormData.get('csrfmiddlewaretoken'));

            xhr.upload.onprogress = function (e) {
            progress(e.loaded / e.total * 100);
            };

            xhr.onload = function() {
            var json;

            if (xhr.status === 400) {
                const errorMessage = xhr.responseText;
                const jsonResponse = JSON.parse(errorMessage);
                failure('Error: ' + jsonResponse["file"]);
                return;
            }

            if (xhr.status === 403) {
                failure('HTTP Error: ' + xhr.status, { remove: true });
                return;
            }

            if (xhr.status < 200 || xhr.status >= 300) {
                failure('HTTP Error: ' + xhr.status);
                return;
            }

            json = JSON.parse(xhr.responseText);

            if (!json || typeof json.location != 'string') {
                failure('Invalid JSON: ' + xhr.responseText);
                return;
            }

            success(json.location);
            };

            xhr.onerror = function () {
            failure('Image upload failed due to a XHR Transport error. Code: ' + xhr.status);
            };

            formData = new FormData();
            formData.append('file', blobInfo.blob(), blobInfo.filename());

            xhr.send(formData);
        }
    ''',
    'content_css': "http://localhost:8000/static/article/css/create_article_content_field.css",
    'setup': '''
        function (editor) {
            const contentErrorMessageContainer = document.querySelectorAll(".content_container span");
            editor.on('click', () => {
                if (contentErrorMessageContainer.length > 0) {
                    contentErrorMessageContainer.forEach((span) => {
                        span.style.display = "none";
                    });
                }
            });
            editor.on('keydown', function(e) {
                if (e.keyCode === 13) {
                    editor.execCommand('mceSetCSS', false, 'line-height: 1.5;');
                }
            });
        }
    ''',
}

# TINYMCE_EXTRA_MEDIA = {
#     'css': {
#         'all': ['http://localhost:8000/static/article/css/create_article_content_field.css'],
#     },
#     'js': ['article/js/image_upload_handler.js'],
# }
