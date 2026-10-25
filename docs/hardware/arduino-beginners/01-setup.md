---
description: "Install the Arduino IDE and connect your board on Windows, macOS or Linux."
---

# Install & set up

1. Download and install the [Arduino IDE](https://www.arduino.cc/en/software).
2. Plug in your board with the USB cable.
3. In the IDE, pick your board and port under **Tools**.

=== "Windows"

    TODO: driver notes, if the club's boards need them (e.g. CH340 clones).

=== "macOS"

    TODO: the port shows up as `/dev/cu.usbmodem...` or `/dev/cu.usbserial...`.

=== "Linux"

    Add yourself to the `dialout` group so the IDE can access the port, then log out and back in:

    ```bash
    sudo usermod -aG dialout $USER
    ```
