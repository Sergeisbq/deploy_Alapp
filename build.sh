# #!/usr/bin/env bash
# # exit on error
# set -o errexit

# pip install -r requirements.txt

# python manage.py collectstatic --no-input
# python manage.py migrate

#!/usr/bin/env bash

set -o errexit
/opt/render/project/src/.venv/bin/python -m pip install --upgrade pip
poetry install
python manage.py collectstatic --no-input
python manage.py migrate