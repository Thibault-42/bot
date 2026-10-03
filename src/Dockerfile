FROM debian:bookwork

RUN apt install -y && apt update -y
RUN apt install python3 -y && apt install python3-pip

RUN python3 -m pip install -U discord.py \
	pip install beautifulsoup4


COPY . ./app

EXPOSE 3000

CMD ["python3", "main.py"]