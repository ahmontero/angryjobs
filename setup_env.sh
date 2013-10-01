# Modified from:
# https://github.com/jdonaldson/dotfiles/blob/master/bootstrap/python.sh

# Select current version of virtualenv:
VERSION=1.10.1

# Name your first "bootstrap" environment:
INITIAL_ENV=__venv__

# Options for your first environment:
ENV_OPTS='--no-site-packages --distribute'

# Set to whatever python interpreter you want for your first environment:
PYTHON=$(which python)

URL_BASE=https://pypi.python.org/packages/source/v/virtualenv

# --- Real work starts here ---

echo "[1/5] Grabbing virtualenv $VERSION"
    curl -O $URL_BASE/virtualenv-$VERSION.tar.gz
    tar xzf virtualenv-$VERSION.tar.gz

# Create the first "bootstrap" environment.
echo "[2/5] Creating new virtualenv in $INITIAL_ENV"
    $PYTHON virtualenv-$VERSION/virtualenv.py $ENV_OPTS $INITIAL_ENV

# Install virtualenv into the environment.
echo "[3/5] Installing virtualenv package to $INITIAL_ENV"
    $INITIAL_ENV/bin/pip install virtualenv-$VERSION.tar.gz

echo "[4/5] Installing local pip packages"
    $INITIAL_ENV/bin/pip install -r requirements/local.txt

# Don't need this anymore.
echo "[5/5] Cleaning up"
    rm -rf virtualenv-$VERSION*

echo "To activate environment: source $INITIAL_ENV/bin/activate"


