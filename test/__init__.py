import os
import sys
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"src"
)
sys.path.append(SOURCE_PATH)


# https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure