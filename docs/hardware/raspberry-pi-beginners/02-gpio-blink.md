---
description: "Wire an LED to a Raspberry Pi and blink it from Python with gpiozero."
---

# Blink an LED with GPIO

Wire an LED and a 330 Ω resistor to GPIO 17, then blink it from Python using [gpiozero](https://gpiozero.readthedocs.io/).

!!! note "TODO"
    Add a wiring diagram to `images/`.

## Starter code

```python title="blink.py"
--8<-- "code/hardware/raspberry-pi-beginners/02-gpio-blink/starter/blink.py"
```

??? success "Solution"

    ```python title="blink.py"
    --8<-- "code/hardware/raspberry-pi-beginners/02-gpio-blink/solution/blink.py"
    ```

Run it on the Pi:

```bash
python3 blink.py
```

Press ++ctrl+c++ to stop.
