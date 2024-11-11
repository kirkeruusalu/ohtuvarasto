from varasto import Varasto


def create_varasto_objects():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    return mehua, olutta


def print_varasto_info(varasto, name):
    print(f"{name} after creation:")
    print(f"{name}: {varasto}")
    print(f"saldo = {varasto.saldo}")
    print(f"tilavuus = {varasto.tilavuus}")
    print(f"paljonko_mahtuu = {varasto.paljonko_mahtuu()}")


def handle_error_case():
    print("Virhetilanteita:")
    huono = Varasto(-100.0)
    print(huono)

    huono = Varasto(100.0, -50.7)
    print(huono)


def perform_operations_on_varastot(mehua, olutta):
    print(f"Olutvarasto: {olutta}")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

    print(f"Olutvarasto: {olutta}")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


def main():
    mehua, olutta = create_varasto_objects()
    print_varasto_info(mehua, "Mehuvarasto")
    print_varasto_info(olutta, "Olutvarasto")
    handle_error_case()
    perform_operations_on_varastot(mehua, olutta)


if __name__ == "__main__":
    main()
