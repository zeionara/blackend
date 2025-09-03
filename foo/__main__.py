from click import argument, group


@group()
def main():
    pass


@main.command()
@argument("messages", type=str, nargs=-1)
def echo(messages: tuple[str, ...]):
    for message in messages:
        print(message)


if __name__ == "__main__":
    main()
