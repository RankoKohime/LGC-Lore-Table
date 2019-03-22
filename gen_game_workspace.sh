#!/bin/bash

# Sets up working enviornment for LGC Game

cd ~/Workspace
git clone git@github.com:EpicGames/UnrealEngine.git
cd UnrealEngine
./Setup.sh
./GenerateProjectFiles.sh
make
#git clone
