    #!/usr/bin/env bash

    echo "Building the project..."

    ## Set up the environment
    if [ ! -d "env" ]; then
        python3 -m venv env
        source env/bin/activate
        pip install -r requirements.txt
    fi

    ## Activate the virtual environment
    source env/bin/activate

    ## Updating Repository
    git pull origin main

    # Build the project
    cd web
    mkdocs build
    cd ..

    ## Deactivate the virtual environment
    deactivate
    echo "Build complete."
    exit 0