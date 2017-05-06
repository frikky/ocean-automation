FROM python:2.7-slim

WORKDIR /app
ADD eula.txt /app/eula.txt

RUN apt-get update -y
RUN apt install default-jre -y
RUN apt install wget -y
RUN wget https://s3.amazonaws.com/Minecraft.Download/versions/1.11.2/minecraft_server.1.11.2.jar

EXPOSE 25565

CMD ["java", "-jar", "minecraft_server.1.11.2.jar", "nogui"]
