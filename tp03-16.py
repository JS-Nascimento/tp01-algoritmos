def inverter_string(string):

    if string == "":
        return ""
    return string[-1] + inverter_string(string[:-1])

if __name__ == "__main__":
    original = "recursao"
    invertida = inverter_string(original)
    print(f"String original: {original}")
    print(f"String invertida: {invertida}")
