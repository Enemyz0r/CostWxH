def wXh(tilePrice, height, width):
    """Function that calculates total price of tiles, width and height

    Args:
        tilePrice - price of a tile
        height - height size
        width - width size

    Returns:
        Calculation of total height, width and tilePrice
    """
    return ((height * width) * tilePrice)


def main():
    wXh(tilePrice, height, width)

if __name__=='__main__':
    main()
