from setuptools import setup, find_packages

setup(name="saaskit-core",
            version="0.1",
            description="Core of saaskit",
            author="CrowdSense",
            author_email="admin@crowdsense.com",
            packages=find_packages(),
            include_package_data=True,
            install_requires = [
                    'setuptools',
                    'django',
                    'python-openid',
                    'django-autoslug',
                    'django-compress',
                    'django-debug-toolbar',
                    'django-extensions',
                    'django-filter',
                    'django-mailer',
                    'django-mptt',
                    'django-notification',
                    'django-oembed',
                    'django-page-cms',
                    'django-perfect404',
                    'django-piston',
                    'django-rosetta',
                    'django-tagging',
                    'django-templatesadmin',
                    'django-uni-form',
                    'html5lib',
                    'python-dateutil',
                    'sorl-thumbnail',
            ],
)

