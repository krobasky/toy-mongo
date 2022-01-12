# Redis for Python using Docker, simple example

## Requirements:
 -  miniconda version 4.11.0+
 -  docker 20.10.11 (for Windows 10+, 16GB RAM+, recommend WSL2 and docker desktop)
 -  docker-compose 3.2 (for Windows/WSL, docker-compose is packaged with docker desktop)

```
conda create -n mongo python
conda activate mongo
conda install --file requirements.txt
```
## Build container
```
docker-compose up --build -d
```

## Confirm build

We changed the port mapping inside the docker-compose file to avoid conflicts with other mongodb servers on the same localhost. Warning - for simplicity, there's no authentication.

```
mongo localhost:27020
# wait for prompt >
use toys
db.createCollection("vintage_dolls")
db.vintage_dolls.insertMany([ {name: "Raggedy Ann", type: "play", year: 1880}, {name: "Dawn", type: "fashion", year: 1970}, {name: "The Lawyers", type: "Kewpie", year: 1912} ])
db.vintage_dolls.find().pretty()                                                                                                               

```
^D out of client


## Demonstration


## Clean-up


```
docker-compose down
```
confirm:
```
docker network ls
docker ps
```
If toy-mongo network remains (e.g., due to `container stop`), remove with:
```
docker network rm `docker network ls|grep toy-mongo|cut -d ' ' -f 1`
docker prune
conda deactivate 
# optionally: conda env remove -n mongo
```
