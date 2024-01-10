from radiant.compiler import server
import sys
import os

sys.path.append(os.path.abspath('.'))
server.main("test_project", ip='localhost', port=5000)
