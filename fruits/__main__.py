"""python -m fruits 入口"""
import sys
from .cli import run

run(sys.argv[1:])
