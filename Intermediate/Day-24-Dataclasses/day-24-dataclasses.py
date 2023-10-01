from dataclasses import dataclass


@dataclass
class Person:
    """Dataclass to store information about a person."""

    name: str
    age: int

    def greet(self, other: "Person") -> None:
        """Greet other person by name."""
        print(f"{self.name} says hi to {other.name}.")


if __name__ == "__main__":
    alice = Person("Alice", 25)
    bob = Person("Bob", 32)
    bob.greet(alice)
