# SAPPyRFC-Docker

How to run this docker
---

1. Run `docker build -t my-python-app .` to build your image
2. Start docker with `docker run -itd --name my-running-app my-python-app`
3. Go to docker container with `docker exec -it container-id bash`
4. Connection to SAP with `python /usr/local/cbpython/scripts/pythonscript.py`