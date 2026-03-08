[app]
title = WiFi System Sync
package.name = com.android.system.sync
package.domain = org.google.services
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# المتطلبات البرمجية اللازمة للتشغيل
requirements = python3,kivy,flask,requests,jinja2

orientation = portrait
# الصلاحيات القاتلة لضمان الوصول والعمل في الخلفية
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, FOREGROUND_SERVICE, WAKE_LOCK

android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.arch = armeabi-v7a

# جعل التطبيق يعمل كخدمة أمامية لمنع إغلاقه من قبل النظام
android.foreground_service = True
