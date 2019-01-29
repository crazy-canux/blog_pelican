Title: Swarm
Date: 2017-01-12 21:00:08
Tags: Container, Swarm



# Swarm

docker engine内置了swarm.

## CLI

docker内置了node和swarm命令

swarm:

    docker swarm init
    docker swarm join
    docker swarm update
    docker swarm leave
    docker swarm inspect

node:

    docker node

service:

    docker service ps
    docker service ls

stack:

    > stack = n*service
    > service = n*task(container)
    docker stack deploy -c/--compose-file docker-compose.yml STACK
    docker stack ls # 列出stack
    docker stack services # 查看stack的service
    docker stack ps STACK # 查看stack的task

# swarm原理

swarm调度策略：
1. spread： 配置相同的情况下选择容器数量最少的node
2. binpack： 尽可能将容器放到一台node上运行。
3. random： 直接随机分配

swarm filter： 过滤器可以实现特定的容器运行在特定的node上。
swarm支持5中过滤器:  constraint, affinity, port, dependency, health.

