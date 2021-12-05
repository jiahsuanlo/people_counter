#!/bin/sh
if [ -v ZSH_VERSION ]
then
    # Assume that this script is executed by zsh
    THIS_DIRECTORY=${0:a:h}
else
    # Assume that this script is executed by bash
    THIS_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null && pwd)"
fi

# activate virtual environment
source .venv/bin/activate

# add formats directory to current python path (in order to read capture files=)

COMMON_DIRECTORY="${THIS_DIRECTORY}"
PYTHONPATH="${COMMON_DIRECTORY}:${PYTHONPATH}"

export PYTHONPATH