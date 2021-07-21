class ScalarTextExpression:
    scalar: str = None


class TextExpression:
    concat: list[ScalarTextExpression] = []

    def add_scalar(self, scalar: str):
        new_scalar = ScalarTextExpression()
        new_scalar.scalar = scalar
        self.concat.append(new_scalar)
