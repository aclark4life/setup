#!/usr/bin/python3
"""Blank the GNOME login keyring password and enable GNOME Desktop Sharing (RDP)."""
import getpass
import os
import subprocess

import dbus

os.environ.setdefault("DBUS_SESSION_BUS_ADDRESS", f"unix:path=/run/user/{os.getuid()}/bus")
bus = dbus.SessionBus()
svc_obj = bus.get_object("org.freedesktop.secrets", "/org/freedesktop/secrets")
svc = dbus.Interface(svc_obj, "org.freedesktop.Secret.Service")
internal = dbus.Interface(
    svc_obj, "org.gnome.keyring.InternalUnsupportedGuiltRiddenInterface"
)
_, session = svc.OpenSession("plain", dbus.String("", variant_level=1))
login = dbus.ObjectPath("/org/freedesktop/secrets/collection/login")


def secret(value):
    return dbus.Struct(
        (session, dbus.ByteArray(b""), dbus.ByteArray(value.encode()), "text/plain"),
        signature="oayays",
    )


old = getpass.getpass("Current Zorin login password (unlocks keyring): ")
internal.ChangeWithMasterPassword(login, secret(old), secret(""))
internal.UnlockWithMasterPassword(login, secret(""))
print("Keyring password is now blank and the keyring is unlocked.")

default_user = getpass.getuser()
user = input(f"Desktop Sharing RDP username [{default_user}]: ").strip() or default_user
pw = getpass.getpass("Desktop Sharing RDP password: ")
for args in (
    ["rdp", "set-credentials", user, pw],
    ["rdp", "disable-view-only"],
    ["rdp", "enable"],
):
    subprocess.run(["grdctl", *args], check=True)
subprocess.run(
    ["systemctl", "--user", "enable", "--now", "gnome-remote-desktop"], check=True
)
subprocess.run(["systemctl", "--user", "restart", "gnome-remote-desktop"], check=True)
print("Desktop Sharing enabled.")
