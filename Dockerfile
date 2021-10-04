FROM ubuntu:21.10
LABEL email="lucasmfpiu@gmail.com"
LABEL git="le314u"
ENV PS1="\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\[\033[1;32m\]\u\[\033[00m\] [\[\033[1;34m\]\w\[\033[00m\]] >"
RUN apt-get update && apt-get install -y python3 && apt-get install -y python3-pip && apt-get clean
COPY proxyCardMTG/* /home/proxyCardMTG/
RUN pip3 install -r requirements.txt
VOLUME ["/Deck"]
ENTRYPOINT ["python3","main.py"]

