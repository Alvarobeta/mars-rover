from dataclasses import dataclass

@dataclass
class Steps:
    steps: str

    def __str__(self) -> str:
        return f"Steps(steps={self.steps})"
