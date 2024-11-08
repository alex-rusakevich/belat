from belat.settings import SCHEMES


def main():
    print("Press Ctrl-C, Ctrl-Z or Ctrl-D to stop")

    while True:
        scheme = SCHEMES[input("Module name: ").lower().strip()]

        tr_direction = (
            input("Direction (cyr-to-lat (ctl) or lat-to-cyr (ltc)): ").lower().strip()
        )

        if tr_direction in ("ctl", "cyr-to-lat"):
            print("Result:", scheme.cyr_to_lat(input("Text: ")))
        elif tr_direction in ("ltc", "lat-to-cyr"):
            print("Result:", scheme.lat_to_cyr(input("Text: ")))


if __name__ == "__main__":
    main()
