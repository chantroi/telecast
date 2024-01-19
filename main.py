from flask import Flask, request, Response
import subprocess

app = Flask("__telestream__")

def executor(chat, url, session, as_chat):
    process = subprocess.Popen(["python3", "-u", "client.py", f"{chat}", f"{url}", f"{session}", f"{as_chat}"], stdout=subprocess.PIPE, universal_newlines=True)
    for line in process.stdout:
        yield line + "\n"
    process.wait()

@app.route("/")
def telestream__():
    chat = request.args.get("chat")
    url = request.args.get("url")
    session = request.args.get("session")
    as_chat = request.args.get("as")
    if not chat:
        return "Cần tham số chat=(username hoặc id của nhóm, channel)"
    if not url:
        return "Cần tham số url=(Liên kết video/âm thanh để phát trực tiếp)"
    if not session:
        return "Thiếu session=(session string)"
    return Response(executor(chat, url, session, as_chat), content_type="text/plain")