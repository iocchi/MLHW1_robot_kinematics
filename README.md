# Robot kinematics exercises

# Preliminary

Download [MLexercises repository](https://github.com/iocchi/MLexercises)  and build its docker image `mlnotebook`.

Check `mlnotebook` image

    docker image ls mlnotebook

# Build robot gym docker image

    ./build.bash

Check `mlrobotgymenvs` image

    docker image ls mlrobotgymenvs

# Run the image

    ./run.bash


# Run robot simulations 

Run inside the container

    python run.py [options]


        usage: run.py [-h] [-env ENV] [-steps STEPS] [-seed SEED] [--render] [--log]

        optional arguments:
          -h, --help    show this help message and exit
          -env ENV      environment [r2,r3,r5] (default: r2)
          -steps STEPS  Execution steps (default: 10,000)
          -seed SEED    Random seed (default: 1000)
          --render      Enable rendering
          --log         Enable data log


Press 'ESC' in the GUI or CTRL-C in the terminal to exit the simulation 

Example:

    python run.py -env r2 -seed 1000 -steps 100000 --render


Environments:

    r2: 2D robot with 2 joints
    r3: 2D robot with 3 joints
    r5: 3D robot with 5 joints
    
Log data

    python run.py -env r2 -seed 1000 -steps 100000 --log > logfile.csv

 
# Colab local runtime

Run the server from the container

    jupyter notebook --ip=0.0.0.0 --no-browser --NotebookApp.allow_remote_access=True --allow-root --NotebookApp.allow_origin='https://colab.research.google.com' --port=8888 --NotebookApp.port_retries=0
    

 
