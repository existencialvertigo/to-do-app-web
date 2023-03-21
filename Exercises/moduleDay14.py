boiling = 100
freezing = 0


def water_state(temperature):
    """ With the water temperature determine
    it's physical state."""
    if temperature <= freezing:
        print("Solid")
    elif boiling > temperature > freezing:
        print("Liquid")
    else:
        print("Gas")
